import json

from settings.base import LOGGER
from utils.encoder import Encoder


class Parser:

    @staticmethod
    def raw_to_json(data: dict) -> dict:
        parsed_data = json.dumps(data, cls=Encoder)
        return json.loads(parsed_data)

    def payload(self, data: dict, field_set: set):
        LOGGER.debug('Cleaning payload data')
        self.__fields_to_remove(data=data, field_set=field_set)

    def __fields_to_remove(self, data: dict, field_set: set):
        fields_to_remove_from_data = set(data.keys()).difference(field_set)
        for field in fields_to_remove_from_data:
            del data[field]
