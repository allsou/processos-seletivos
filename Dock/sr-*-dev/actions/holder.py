import traceback
from json import JSONDecodeError

from mongoengine.errors import NotUniqueError

from exceptions.account import (AccountActiveException,
                                AccountHasBalanceException)
from exceptions.general import InvalidFieldsValuesException, NotFoundException
from services.holder import HolderService
from settings.base import LOGGER
from utils.messages import CRITICAL_ERROR, INVALID_PAYLOAD
from utils.response_generator import generate_response


class HolderAction:

    async def create(self, request):
        try:
            LOGGER.debug('Creating holder action')
            payload = await request.json()
            holder = HolderService().create_holder(data=payload)
            return generate_response(data=holder, status_code=201)

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

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def delete(self, request):
        try:
            LOGGER.debug('Delete holder action')
            tax_id = request.path_params.get('tax_id')
            await HolderService().delete_holder(tax_id)
            return generate_response()

        except NotFoundException as exception:
            return generate_response(
                status_code=404, message=[exception.message])

        except (AccountHasBalanceException,
                AccountActiveException) as exception:
            return generate_response(
                status_code=400, message=[exception.message])

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])
