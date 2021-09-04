from mongoengine import (
    Document,
    StringField,
    DecimalField
)


class Product(Document):
    price = DecimalField(required=True, min_value=0.01, precision=2)
    image = StringField(required=True, min_length=1, max_length=400)
    brand = StringField(required=True, min_length=1, max_length=400)
    title = StringField(required=True, min_length=1, max_length=400)
    reviewScore = DecimalField(min_value=0.01, max_value=5, precision=2)

    def clean(self):
        self.brand = self.brand.upper()
        self.title = self.title.upper()

