from utils.messages import REQUIRED_FIELD


class MissingRequiredFieldsException(Exception):
    def __init__(self, fields: set):
        self.messages = [{**REQUIRED_FIELD, 'field': field} for field in fields]
