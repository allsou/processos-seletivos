import re

from mongoengine import (
    Document,
    StringField,
    ListField
)

EMAIL_REGEX = re.compile(
    r'^((?!\.)[\w_.]*[^.])((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})'
    r'|@(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
)


class Customer(Document):
    name = StringField(required=True, min_length=1, max_length=120)
    email = StringField(required=True, regex=EMAIL_REGEX, unique=True)
    favorites = ListField()

    def clean(self):
        self.name = self.name.upper()
        self.email = self.email.lower()
