import decimal
from datetime import datetime
from enum import Enum

from mongoengine import (DateTimeField, DecimalField, Document, EnumField,
                         StringField)

CREATE_TRANSACTION_ALLOWED_FIELDS = {
    "value",
    "method"
}


class Method(Enum):
    CREDIT = 'credit'
    DEBIT = 'debit'


class Transaction(Document):
    value = DecimalField(required=True, precision=2,
                         min_value=0.001, rounding=decimal.ROUND_FLOOR)
    account_number = StringField(required=True)
    account_agency = StringField(required=True)
    method = EnumField(
        Method, choices=[Method.CREDIT, Method.DEBIT],
        required=True)
    created_at = DateTimeField(default=datetime.now())
