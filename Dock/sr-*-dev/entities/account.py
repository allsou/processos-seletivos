from mongoengine import BooleanField, Document, ObjectIdField, StringField

CREATE_ACCOUNT_ALLOWED_FIELDS = {
    'tax_id'
}


class Account(Document):
    number = StringField(required=True, min_length=11, max_length=11)
    agency = StringField(required=True, default='0001')
    active = BooleanField(default=True)
    blocked = BooleanField(default=False)
    holder_id = ObjectIdField(required=True, unique=True)
