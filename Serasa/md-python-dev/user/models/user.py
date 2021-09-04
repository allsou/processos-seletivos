"""
Model to represent user entity
"""
import json
import re
from datetime import datetime

from mongoengine import Document, EmailField, DateTimeField, StringField, ListField


class User(Document):
    name = StringField(min_length=1)
    cpf = StringField(unique=True, max_length=11, min_length=11)
    email = EmailField()
    phone_number = StringField(regex=re.compile('(\\(\\d{2}\\)\\s)(\\d{4,5}\\-\\d{4})'))
    created_at = DateTimeField(default=datetime.now())
    updated_at = ListField()

    def populate(self, data: dict):
        """

        Args:
            data: data from request

        Returns: None

        """
        fields = []
        for field, value in data.items():
            if field == 'name':
                self.name = value
                fields.append('name')
            elif field == 'email':
                self.email = value
                fields.append('email')
            elif field == 'phone_number':
                self.phone_number = value
                fields.append('phone_number')
        if fields:
            self.__update_at(fields)

    def __update_at(self, fields: list):
        """

        Args:
            fields: object fields list

        Returns:

        """
        self.updated_at.append(
            {
                'datetime': datetime.now(),
                'fields': fields
            }
        )

    def to_response(self):
        """

        Returns: Json encoded object

        """
        user = json.loads(self.to_json())
        user['created_at'] = user.get('created_at').get('$date')
        user['_id'] = user.get('_id').get('$oid')
        return user
