import traceback
from json import JSONDecodeError

from exceptions.general import NotFoundException
from exceptions.payloads import MissingRequiredFieldsException
from exceptions.products import InvalidFieldsValuesException
from services.auth import requires_auth
from services.product import ProductService
from settings import LOGGER
from utils.messages import CRITICAL_ERROR, INVALID_PAYLOAD
from utils.response_generator import generate_response


class ProductAction:

    @requires_auth
    async def create_product(self, request):
        try:
            LOGGER.debug('Creating product action')
            payload = await request.json()
            product = ProductService().create_product(data=payload)
            return generate_response(data=product, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except InvalidFieldsValuesException as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    @requires_auth
    async def get_product(self, request):
        try:
            LOGGER.debug('Getting product by id action')
            product_id = request.path_params.get('product_id')
            product = ProductService().get_product(product_id=product_id)
            return generate_response(data=product)
        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except NotFoundException:
            return generate_response(status_code=404)

        except InvalidFieldsValuesException as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    @requires_auth
    async def delete_product(self, request):
        try:
            LOGGER.debug('Delete product action')
            product_id = request.path_params.get('product_id')
            ProductService().delete_product(product_id=product_id)
            return generate_response(data={'_id': product_id})
        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except NotFoundException:
            return generate_response(status_code=404)

        except InvalidFieldsValuesException as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    @requires_auth
    async def update_product(self, request):
        try:
            LOGGER.debug('Update product action')
            product_id = request.path_params.get('product_id')
            payload = await request.json()
            product = ProductService().update_product(data=payload, product_id=product_id)
            return generate_response(data=product)
        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except NotFoundException:
            return generate_response(status_code=404)

        except InvalidFieldsValuesException as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    @requires_auth
    async def get_products(self, request):
        try:
            LOGGER.debug('Getting products action')
            page = request.query_params.get('page')
            products = ProductService().get_products(page=page)
            return generate_response(data=products)
        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except NotFoundException:
            return generate_response(status_code=404)

        except InvalidFieldsValuesException as exception:
            return generate_response(message=exception.messages, status_code=422)
        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])