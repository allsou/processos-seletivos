import traceback
from json import JSONDecodeError

from mongoengine.errors import NotUniqueError

from exceptions.general import InvalidFieldsValuesException, NotFoundException
from exceptions.transaction import (DailyLimitException,
                                    InvalidDateParamsException,
                                    NotBalanceEnoughException,
                                    TransactionNotAllowedException)
from services.account import AccountService
from services.transaction import TransactionService
from settings.base import LOGGER
from utils.messages import CRITICAL_ERROR, INVALID_PAYLOAD
from utils.response_generator import generate_response


class AccountAction:

    async def create_account(self, request):
        try:
            LOGGER.debug('Creating account action')
            payload = await request.json()
            account = await AccountService().create_account(data=payload)
            return generate_response(data=account, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(
                message=[INVALID_PAYLOAD],
                status_code=400)

        except InvalidFieldsValuesException as exception:
            return generate_response(
                message=exception.messages, status_code=422)

        except NotUniqueError:
            return generate_response(
                message=[{'message': 'Tax id alredy in use'}],
                status_code=400)

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def create_transaction(self, request):
        try:
            LOGGER.debug('Creating transaction action')
            payload = await request.json()
            agency = request.path_params.get('agency')
            number = request.path_params.get('number')
            transaction = await TransactionService().create_transaction(
                agency=agency,
                number=number,
                data=payload
            )
            return generate_response(data=transaction, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(
                message=[INVALID_PAYLOAD],
                status_code=400)

        except InvalidFieldsValuesException as exception:
            return generate_response(
                message=exception.messages, status_code=422)

        except NotUniqueError:
            return generate_response(
                message=[{'message': 'Tax id alredy in use'}],
                status_code=400)

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except (TransactionNotAllowedException,
                DailyLimitException,
                NotBalanceEnoughException) as exception:
            return generate_response(
                status_code=401, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def get_balance(self, request):
        try:
            LOGGER.debug('Getting balance action')
            agency = request.path_params.get('agency')
            number = request.path_params.get('number')
            balance = await TransactionService().get_transaction_balance(
                agency=agency,
                number=number
            )
            return generate_response(
                data={'balance': balance},
                status_code=200)

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def get_transactions(self, request):
        try:
            LOGGER.debug('Getting transactions action')
            agency = request.path_params.get('agency')
            number = request.path_params.get('number')
            begin_date = request.query_params.get('begin_date')
            end_date = request.query_params.get('end_date')
            _, transactions = await TransactionService().get_transactions(
                agency, number, begin_date, end_date
            )
            return generate_response(
                data=transactions,
                status_code=200)

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except InvalidDateParamsException as exception:
            return generate_response(
                status_code=400, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def change_account_active_status(self, request):
        try:
            LOGGER.debug('Changing account status action')
            agency = request.path_params.get('agency')
            number = request.path_params.get('number')
            transactions = await AccountService().change_active_status(
                agency, number
            )
            return generate_response(
                data=transactions,
                status_code=200)

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def change_account_block_status(self, request):
        try:
            LOGGER.debug('Changing account block status action')
            agency = request.path_params.get('agency')
            number = request.path_params.get('number')
            transactions = await AccountService().change_block_status(
                agency, number
            )
            return generate_response(
                data=transactions,
                status_code=200)

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])
