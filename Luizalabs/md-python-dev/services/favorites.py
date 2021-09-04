import traceback

from mongoengine.errors import ValidationError, NotUniqueError

from connections.database import Database
from exceptions.customer import EmailAlreadyUsedException
from exceptions.payloads import MissingRequiredFieldsException
from exceptions.products import InvalidFieldsValuesException
from parsers.general import Parser
from settings import LOGGER
from validations.favorites import FavoriteValidations


class FavoritesService:
    def __init__(self):
        self.__database = Database()
        self.__parser = Parser()
        self.__validations = FavoriteValidations()

    def insert_favorite(self, product_id: str, customer_id: str):
        try:
            LOGGER.debug('Inserting product to customer list')
            self.__validations.validate_customer_product_id(product_id=product_id, customer_id=customer_id)
            customer = self.__database.get_customer_by_id(customer_id=customer_id)
            product = self.__database.get_product_by_id(product_id=product_id)
            customer = self.__database.push_product_to_favorites(customer=customer, product=product)
            return self.__parser.parse_customer_favorites(customer=customer)

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

    def remove_favorite(self, product_id: str, customer_id: str):
        try:
            LOGGER.debug('Removing product to customer list')
            self.__validations.validate_customer_product_id(product_id=product_id, customer_id=customer_id)
            customer = self.__database.get_customer_by_id(customer_id=customer_id)
            product = self.__database.get_product_by_id(product_id=product_id)
            customer = self.__database.pull_product_to_favorites(customer=customer, product=product)
            return self.__parser.parse_customer_favorites(customer=customer)

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
