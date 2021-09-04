from utils.messages import INVALID_PARAM_VALUE, REQUIRED_FIELD


class InvalidRecordException(Exception):
    def __init__(self):
        self.messages = [{**INVALID_PARAM_VALUE, 'field': 'market_register'}]


class NotFoundException(Exception):
    pass


class MissingRequiredFieldsException(Exception):
    def __init__(self, fields: set):
        self.messages = [{**REQUIRED_FIELD, 'field': field} for field in fields]