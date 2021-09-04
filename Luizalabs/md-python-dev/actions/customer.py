import traceback
from json import JSONDecodeError

from pymongo.errors import DuplicateKeyError

from exceptions.customer import EmailAlreadyUsedException
from exceptions.general import NotFoundException
from exceptions.payloads import MissingRequiredFieldsException
from exceptions.products import InvalidFieldsValuesException
from services.auth import requires_auth
from services.customer import CustomerService
from settings import LOGGER
from utils.messages import CRITICAL_ERROR, INVALID_PAYLOAD
from utils.response_generator import generate_response


class CustomerAction:

    @requires_auth
    async def create_customer(self, request):
        try:
            LOGGER.debug('Creating customer action')
            payload = await request.json()
            customer = CustomerService().create_customer(data=payload)
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
    async def get_customer(self, request):
        try:
            LOGGER.debug('Getting customer by id action')
            customer_id = request.path_params.get('customer_id')
            customer = CustomerService().get_customer(customer_id=customer_id)
            return generate_response(data=customer)
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
    async def delete_customer(self, request):
        try:
            LOGGER.debug('Delete customer action')
            customer_id = request.path_params.get('customer_id')
            CustomerService().delete_customer(customer_id=customer_id)
            return generate_response(data={'_id': customer_id})
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
    async def update_customer(self, request):
        try:
            LOGGER.debug('Update customer action')
            customer_id = request.path_params.get('customer_id')
            payload = await request.json()
            customer = CustomerService().update_customer(data=payload, customer_id=customer_id)
            return generate_response(data=customer)
        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except NotFoundException:
            return generate_response(status_code=404)

        except (InvalidFieldsValuesException, EmailAlreadyUsedException) as exception:
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])
