from exceptions.payloads import MissingRequiredFieldsException
from settings import LOGGER

AUTHORIZED_IMAGE_TYPES = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'bmp', 'png']

CREATE_CUSTOMER_ALLOWED_FIELDS = {
    "name",
    "email"
}


class CustomerValidations:
    def __init__(self):
        self.__field_set_data_at_creation = CREATE_CUSTOMER_ALLOWED_FIELDS.copy()

    def data(self, data: dict, is_update: bool = False):
        LOGGER.debug('Validating create data')
        self.__set_difference(field_set=self.__field_set_data_at_creation, data=data, is_update=is_update)

    def __set_difference(self, field_set: set, data: dict, is_update: bool):
        difference = field_set.difference(data.keys())
        if difference and not is_update:
            LOGGER.debug('Missing field in data payload')
            raise MissingRequiredFieldsException(fields=difference)
        self.__fields_to_remove(data=data, field_set=field_set)

    def update_data(self, data: dict):
        LOGGER.debug('Validating update data')
        self.__fields_to_remove(data=data, field_set=self.__field_set_data_at_creation)

    def __fields_to_remove(self, data: dict, field_set: set):
        fields_to_remove_from_data = set(data.keys()).difference(field_set)
        for field in fields_to_remove_from_data:
            del data[field]
