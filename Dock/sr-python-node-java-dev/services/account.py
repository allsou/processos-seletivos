import re
import traceback
from xml.dom.minidom import Document

from mongoengine.errors import NotUniqueError, ValidationError

from connections.database import Database
from entities.account import CREATE_ACCOUNT_ALLOWED_FIELDS, Account
from entities.holder import Holder
from exceptions.general import (InvalidFieldsValuesException,
                                MissingRequiredFieldsException)
from parsers.general import Parser
from settings.base import LOGGER


class AccountService:
    def __init__(self):
        self.__database = Database()
        self.__parser = Parser()

    async def create_account(self, data: dict):
        try:
            LOGGER.debug('Creating account service')
            self.__parser.payload(
                data, field_set=CREATE_ACCOUNT_ALLOWED_FIELDS)
            holder = self.__database.get(document_type=Holder, query={
                'tax_id': re.sub("[^0-9]", '', data.get('tax_id', ''))
            })
            holder = Account(number=holder.tax_id, holder_id=holder.id)
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

    async def change_active_status(self, agency: str, number: str):
        try:
            LOGGER.debug('Change account status service')
            account = self.__change_boolean_field(agency, number, 'active')
            return self.__parser.raw_to_json(
                data=account.to_mongo().to_dict())

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    async def change_block_status(self, agency: str, number: str):
        try:
            LOGGER.debug('Change account block status service')
            account = self.__change_boolean_field(agency, number, 'blocked')
            return self.__parser.raw_to_json(
                data=account.to_mongo().to_dict())

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(exception)
            raise exception

    def __change_boolean_field(
            self, agency: str, number: str, field: str) -> Document:

        account = self.__database.get(
            document_type=Account,
            query={
                'number': number,
                'agency': agency
            }
        )
        account.update(**{field: not getattr(account, field)})
        return account.reload()
