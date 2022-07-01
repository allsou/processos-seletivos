import traceback

from mongoengine.errors import NotUniqueError, ValidationError

from connections.database import Database
from entities.account import Account
from entities.holder import CREATE_HOLDER_ALLOWED_FIELDS, Holder
from exceptions.account import (AccountActiveException,
                                AccountHasBalanceException)
from exceptions.general import (InvalidFieldsValuesException,
                                MissingRequiredFieldsException,
                                NotFoundException)
from parsers.general import Parser
from services.transaction import TransactionService
from settings.base import LOGGER


class HolderService:
    def __init__(self):
        self.__database = Database()
        self.__parser = Parser()

    def create_holder(self, data: dict) -> dict:
        try:
            LOGGER.debug('Creating holder service')
            self.__parser.payload(data, field_set=CREATE_HOLDER_ALLOWED_FIELDS)
            holder = Holder(**data)
            holder = self.__database.save(document=holder)
            return self.__parser.raw_to_json(
                data=holder.to_mongo().to_dict())

        except NotUniqueError:
            LOGGER.info('Tax id already in use')
            raise

        except ValidationError as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.debug('Invalid fields value')
            raise InvalidFieldsValuesException(validations=exception.to_dict())

        except MissingRequiredFieldsException as exception:
            raise exception

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    async def delete_holder(self, tax_id: str):
        try:
            LOGGER.debug('Deleting holder service')
            holder = self.__database.get(
                document_type=Holder, query={'tax_id': tax_id})
            try:
                account = self.__database.get(document_type=Account, query={
                                              'holder_id': holder.id})
                if account.active:
                    LOGGER.info('Account active, disable before delete holder')
                    raise AccountActiveException
                balance = await TransactionService().get_transaction_balance(
                    agency=account.agency, number=account.number
                )
                if balance:
                    LOGGER.info(
                        'Account has balance, withdraw before delete holder')
                    raise AccountHasBalanceException
            except NotFoundException:
                pass
            self.__database.remove(document_type=Holder,
                                   query={'tax_id': tax_id})

        except (NotFoundException,
                AccountHasBalanceException,
                AccountActiveException):
            raise

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception
