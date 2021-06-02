"""
Order entity
"""
from datetime import datetime

from peewee import Model, CharField, IntegerField, FloatField, DateTimeField

from connections.mysql import Mysql


class BaseModel(Model):
    class Meta:
        database = Mysql().database


class Order(BaseModel):
    user_id = CharField()
    item_description = CharField()
    item_quantity = IntegerField()
    item_price = FloatField()
    total_value = FloatField()
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(null=True)

    class Meta:
        db_table = 'orders'
