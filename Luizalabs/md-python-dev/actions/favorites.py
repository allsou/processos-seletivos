import traceback
from json import JSONDecodeError

from pymongo.errors import DuplicateKeyError

from exceptions.customer import EmailAlreadyUsedException
from exceptions.general import NotFoundException
from exceptions.payloads import MissingRequiredFieldsException
from exceptions.products import InvalidFieldsValuesException
from services.auth import requires_auth
from services.favorites import FavoritesService
from settings import LOGGER
from utils.messages import CRITICAL_ERROR, INVALID_PAYLOAD
from utils.response_generator import generate_response


class FavoritesAction:

    @requires_auth
    async def insert_favorite(self, request):
        try:
            LOGGER.debug('Inserting customer favorite product action')
            customer_id = request.path_params.get('customer_id')
            product_id = request.path_params.get('product_id')
            customer = FavoritesService().insert_favorite(product_id=product_id, customer_id=customer_id)
            return generate_response(data=customer, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except DuplicateKeyError:
            return generate_response(message=[{'message': 'Duplicated email'}], status_code=400)

        except (InvalidFieldsValuesException, EmailAlreadyUsedException) as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    @requires_auth
    async def remove_favorite(self, request):
        try:
            LOGGER.debug('Removing customer favorite product action')
            customer_id = request.path_params.get('customer_id')
            product_id = request.path_params.get('product_id')
            customer = FavoritesService().remove_favorite(product_id=product_id, customer_id=customer_id)
            return generate_response(data=customer, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except DuplicateKeyError:
            return generate_response(message=[{'message': 'Duplicated email'}], status_code=400)

        except (InvalidFieldsValuesException, EmailAlreadyUsedException) as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])