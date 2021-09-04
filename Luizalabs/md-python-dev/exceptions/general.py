from utils.messages import INVALID_PARAM_VALUE


class NotFoundException(Exception):
    pass


class InvalidParamValueException(Exception):
    def __init__(self, param: str):
        self.messages = [{**INVALID_PARAM_VALUE, 'param': param}]
