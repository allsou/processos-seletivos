import traceback

from mongoengine.errors import ValidationError

from connections.database import Database
from entities.product import Product
from exceptions.general import NotFoundException
from exceptions.payloads import MissingRequiredFieldsException
from exceptions.products import InvalidFieldsValuesException
from parsers.general import Parser
from settings import LOGGER
from validations.general import is_object_id
from validations.product import ProductValidations


class ProductService:
    def __init__(self):
        self.__database = Database()
        self.__parser = Parser()
        self.__validations = ProductValidations()

    def create_product(self, data: dict):
        try:
            LOGGER.debug('Creating product service')
            self.__validations.product_data(data=data)
            product = Product(**data)
            product = self.__database.save(document=product)
            return self.__parser.raw_to_json(data=product.to_mongo().to_dict())

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

    def get_product(self, product_id: str):
        try:
            is_object_id(object_id=product_id)
            LOGGER.debug(f'Getting product {product_id}')
            product = self.__database.get_product_by_id(product_id=product_id)
            return self.__parser.raw_to_json(data=product.to_mongo().to_dict())

        except NotFoundException as exception:
            raise exception

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    def delete_product(self, product_id: str):
        try:
            is_object_id(object_id=product_id)
            LOGGER.debug(f'Deleting product service {product_id}')
            self.__database.delete_product_by_id(product_id=product_id)

        except NotFoundException as exception:
            raise exception

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    def update_product(self, data: dict, product_id: str):
        try:
            is_object_id(object_id=product_id)
            self.__validations.product_data(data=data, is_update=True)
            LOGGER.debug(f'Updating product service {product_id}')
            product = self.__database.update_product_by_id(product_id=product_id, data=data)
            return self.__parser.raw_to_json(data=product.to_mongo().to_dict())

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

    def get_products(self, page: str):
        try:
            LOGGER.debug('Getting products service')
            parse_page = self.__parser.page(page=page)
            products, products_total = self.__database.get_products(page=parse_page)
            return self.__parser.products(data=list(products.as_pymongo()), total=products_total, page=parse_page)
        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception
