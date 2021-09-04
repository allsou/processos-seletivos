class EmailAlreadyUsedException(Exception):
    def __init__(self):
        self.messages = [{"code": "unique_field", "description": "email already in use"}]
