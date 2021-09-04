import traceback

from mongoengine.errors import ValidationError, NotUniqueError
from connections.database import Database
from entities.customer import Customer
from exceptions.customer import EmailAlreadyUsedException
from exceptions.general import NotFoundException
from exceptions.payloads import MissingRequiredFieldsException
from exceptions.products import InvalidFieldsValuesException
from parsers.general import Parser
from settings import LOGGER
from validations.customer import CustomerValidations
from validations.general import is_object_id


class CustomerService:
    def __init__(self):
        self.__database = Database()
        self.__parser = Parser()
        self.__validations = CustomerValidations()

    def create_customer(self, data: dict):
        try:
            LOGGER.debug('Creating customer service')
            self.__validations.data(data=data)
            customer = Customer(**data)
            customer = self.__database.save(document=customer)
            return self.__parser.raw_to_json(data=customer.to_mongo().to_dict())

        except NotUniqueError:
            LOGGER.info('Email already used')
            raise EmailAlreadyUsedException()

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

    def get_customer(self, customer_id: str):
        try:
            is_object_id(object_id=customer_id)
            LOGGER.debug(f'Getting customer {customer_id}')
            customer = self.__database.get_customer_by_id(customer_id=customer_id)
            return self.__parser.parse_customer_favorites(customer=customer)

        except NotFoundException as exception:
            raise exception

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    def delete_customer(self, customer_id: str):
        try:
            is_object_id(object_id=customer_id)
            LOGGER.debug(f'Deleting customer service {customer_id}')
            self.__database.delete_customer_by_id(customer_id=customer_id)

        except NotFoundException as exception:
            raise exception

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    def update_customer(self, data: dict, customer_id: str):
        try:
            is_object_id(object_id=customer_id)
            self.__validations.data(data=data, is_update=True)
            LOGGER.debug(f'Updating customer service {customer_id}')
            customer = self.__database.update_customer_by_id(customer_id=customer_id, data=data)
            return self.__parser.raw_to_json(data=customer.to_mongo().to_dict())

        except NotUniqueError:
            LOGGER.info('Email already used')
            raise EmailAlreadyUsedException()

        except ValueError:
            LOGGER.debug(traceback.format_exc())
            LOGGER.debug('Invalid fields value')
            raise InvalidFieldsValuesException(validations={'field': ''})

        except ValidationError as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.debug('Invalid fields value')
            raise InvalidFieldsValuesException(validations={exception.field_name: ''})

        except NotFoundException as exception:
            raise exception

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception
