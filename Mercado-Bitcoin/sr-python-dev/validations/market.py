import re

from exceptions.market import InvalidRecordException, MissingRequiredFieldsException
from settings import LOGGER

REGISTRY_FIELD = "registro"
UPDATE_MARKET_ALLOWED_FIELDS = {
    "long",
    "lat",
    "setcens",
    "areap",
    "coddist",
    "distrito",
    "codsubpref",
    "subprefe",
    "regiao5",
    "regiao8",
    "nome_feira",
    "logradouro",
    "numero",
    "bairro",
    "referencia"
}
CREATE_MARKET_ALLOWED_FIELDS = {
    REGISTRY_FIELD,
    *UPDATE_MARKET_ALLOWED_FIELDS
}


class MarketValidations:
    def __init__(self):
        self.__field_set_data_at_creation = CREATE_MARKET_ALLOWED_FIELDS

    @staticmethod
    def is_valid_registry(registry: str):
        match = re.match('\\d{4}-\\d', registry)
        if not match:
            LOGGER.info('Invalid registry, raising exception')
            raise InvalidRecordException()

    def new_market(self, data: dict):
        LOGGER.debug('Validating create data')
        self.__set_difference(field_set=self.__field_set_data_at_creation, data=data)

    def __set_difference(self, field_set: set, data: dict):
        difference = field_set.difference(data.keys())
        if difference:
            LOGGER.debug('Missing field in data payload')
            raise MissingRequiredFieldsException(fields=difference)
        self.__fields_to_remove(data=data, field_set=field_set)

    @staticmethod
    def __fields_to_remove(data: dict, field_set: set):
        fields_to_remove_from_data = set(data.keys()).difference(field_set)
        for field in fields_to_remove_from_data:
            del data[field]

    def update_market(self, data: dict):
        self.__fields_to_remove(data=data, field_set=UPDATE_MARKET_ALLOWED_FIELDS)
