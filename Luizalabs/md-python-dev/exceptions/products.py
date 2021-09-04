from utils.messages import INVALID_FIELD_VALUE


class InvalidFieldsValuesException(Exception):
    def __init__(self, validations: dict):
        self.messages = [{**INVALID_FIELD_VALUE, 'field': key} for key in validations.keys()]

