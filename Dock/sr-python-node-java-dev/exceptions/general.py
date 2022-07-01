from utils.messages import INVALID_FIELD_VALUE, REQUIRED_FIELD


class InvalidFieldsValuesException(Exception):
    def __init__(self, validations: dict):
        self.messages = [{**INVALID_FIELD_VALUE, 'field': key}
                         for key in validations.keys()]


class MissingRequiredFieldsException(Exception):
    def __init__(self, fields: set):
        self.messages = [{**REQUIRED_FIELD, 'field': field}
                         for field in fields]


class NotFoundException(Exception):
    def __init__(self, message: str = None):
        self.message = message
