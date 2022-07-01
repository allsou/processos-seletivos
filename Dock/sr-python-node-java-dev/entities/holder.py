"""
    Dúvidas de requisitos do desafio:
        - Um portador pode ser excluído com contas ativas e/ou com saldo?
            * Será implementado que não será possível se tiver conta ativa ou com saldo # noqa: 501
"""
import re

from mongoengine import Document, StringField

from validations.tax_id import is_tax_id_valid

CREATE_HOLDER_ALLOWED_FIELDS = {
    "name",
    "tax_id"
}


class Holder(Document):
    name = StringField(required=True, min_length=1, max_length=120)
    tax_id = StringField(required=True, unique=True,
                         validation=is_tax_id_valid)

    def clean(self):
        if self.name:
            self.name = self.name.upper()
        if self.tax_id:
            self.tax_id = re.sub("[^0-9]", '', self.tax_id)
