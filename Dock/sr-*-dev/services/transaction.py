import traceback
from datetime import datetime

from mongoengine.errors import NotUniqueError, ValidationError

from connections.cache import Cache
from connections.database import Database
from entities.account import Account
from entities.transaction import (CREATE_TRANSACTION_ALLOWED_FIELDS, Method,
                                  Transaction)
from exceptions.general import (InvalidFieldsValuesException,
                                MissingRequiredFieldsException,
                                NotFoundException)
from exceptions.transaction import (DailyLimitException,
                                    InvalidDateParamsException,
                                    NotBalanceEnoughException,
                                    TransactionNotAllowedException)
from parsers.general import Parser
from settings.base import DAILY_LIMIT, LOGGER

BALANCE_CACHE_KEY = 'balance:{}:{}'
DAILY_DEBIT_BALANCE_CACHE_KEY = 'daily:{}:{}'


class TransactionService:
    def __init__(self):
        self.__database = Database()
        self.__parser = Parser()
        self.__cache = Cache()

    async def create_transaction(self, agency: str, number: str, data: dict):
        try:
            LOGGER.debug('Creating transaction service')

            self.__parser.payload(
                data, field_set=CREATE_TRANSACTION_ALLOWED_FIELDS

            )

            account = self.__database.get(
                document_type=Account,
                query={
                    'number': number,
                    'agency': agency
                }
            )

            if not account.active or account.blocked:
                raise TransactionNotAllowedException

            transaction = Transaction(
                value=data.get('value'),
                account_number=number,
                account_agency=agency,
                method=data.get('method')
            )
            if transaction.method == Method.DEBIT:

                actual_balance = await self.get_transaction_balance(
                    agency, number
                )
                if actual_balance < transaction.value:
                    raise NotBalanceEnoughException

                daily_debit = await self.__get_daily_debit(agency, number)

                if daily_debit > DAILY_LIMIT or float(
                        transaction.value) + daily_debit > DAILY_LIMIT:
                    raise DailyLimitException

            transaction = self.__database.save(document=transaction)

            await self.__update_cache(agency, number)

            return self.__parser.raw_to_json(
                data=transaction.to_mongo().to_dict()
            )

        except NotUniqueError:
            LOGGER.info('Tax id already in use')
            raise

        except ValidationError as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.debug('Invalid fields value')
            raise InvalidFieldsValuesException(validations=exception.to_dict())

        except (MissingRequiredFieldsException,
                TransactionNotAllowedException,
                NotBalanceEnoughException,
                DailyLimitException):
            raise

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    async def __update_cache(self, agency, number):
        LOGGER.debug('Updating cache')

        await self.__update_balance_cache(
            agency,
            number,
            BALANCE_CACHE_KEY.format(agency, number)
        )

        await self.__update_daily_debit_cache(
            agency,
            number,
            DAILY_DEBIT_BALANCE_CACHE_KEY.format(agency, number)
        )

    async def get_transaction_balance(self, agency: str, number: str) -> float:
        try:
            self.__database.get(
                document_type=Account,
                query={
                    'number': number,
                    'agency': agency
                }
            )

            cache_key = BALANCE_CACHE_KEY.format(agency, number)
            balance = self.__cache.get(cache_key)

            if not balance:
                LOGGER.debug('Balance not found on cache')
                balance = await self.__update_balance_cache(
                    agency, number, cache_key)

            return float(balance)

        except NotFoundException:
            raise
        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    async def __update_balance_cache(self, agency, number, cache_key):
        transactions = self.__database.list(
            document_type=Transaction,
            query={
                'account_agency': agency,
                'account_number': number
            }
        )
        _, _, balance = self.__sum_transactions(transactions)
        self.__cache.set(cache_key, balance)
        return balance

    async def __get_daily_debit(self, agency, number):
        daily_debit_cache_key = DAILY_DEBIT_BALANCE_CACHE_KEY.format(
            agency,
            number
        )
        daily_debit = self.__cache.get(daily_debit_cache_key)
        if not daily_debit:
            daily_debit = await self.__update_daily_debit_cache(
                agency, number, daily_debit_cache_key)
        return float(daily_debit)

    async def __update_daily_debit_cache(self, agency, number, cache_key):
        now = datetime.now()
        daily_transactions, _ = await self.get_transactions(
            agency,
            number,
            now.strftime('%d/%m/%Y'),
            now.strftime('%d/%m/%Y')
        )
        _, daily_debit, _ = self.__sum_transactions(
            daily_transactions)
        self.__cache.set(cache_key, daily_debit)
        return daily_debit

    def __sum_transactions(self, transactions: list):
        LOGGER.debug('Generating balance')

        credit = sum(
            list(
                map(
                    lambda statement: statement.value,
                    filter(
                        lambda transaction: transaction.method == Method.CREDIT,  # noqa: 501
                        transactions
                    )
                )
            )
        )

        debit = sum(
            list(
                map(
                    lambda statement: statement.value,
                    filter(
                        lambda transaction: transaction.method == Method.DEBIT,
                        transactions
                    )
                )
            )
        )

        return float(credit), float(debit), float(credit - debit)

    async def get_transactions(
        self, agency: str, number: str, begin_date: str, end_date: str
    ) -> float:
        try:
            end = datetime.strptime(
                end_date, '%d/%m/%Y').replace(hour=23, minute=59, second=59)
            begin = datetime.strptime(
                begin_date, '%d/%m/%Y')

            self.__database.get(
                document_type=Account,
                query={
                    'number': number,
                    'agency': agency
                }
            )

            transactions = self.__database.list(
                document_type=Transaction,
                query={
                    'account_agency': agency,
                    'account_number': number,
                    'created_at__lte': end,
                    'created_at__gte': begin
                }
            )

            return transactions, self.__parser.raw_to_json(
                list(transactions.as_pymongo()))

        except NotFoundException:
            raise

        except (TypeError, ValueError):
            raise InvalidDateParamsException

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception
