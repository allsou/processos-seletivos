import pytest

from entities.order import Order

data = {
    "user_id": "5f276c2523bd3ebf871808c",
    "item_description": " dsa 0asda 0000000191",
    "item_quantity": 4,
    "item_price": 1.99
}


def test_valid_instance_should_assert_correctly():
    order = Order(
        user_id=data.get('user_id'),
        item_description=data.get('item_description'),
        item_quantity=data.get('item_quantity'),
        item_price=data.get('item_price'),
        total_value=(data.get('item_quantity') * data.get('item_price'))
    )
    assert order.user_id == data.get('user_id')
    assert order.item_description == data.get('item_description')
    assert order.item_quantity == data.get('item_quantity')
    assert order.item_price == data.get('item_price')
    assert order.total_value == (data.get('item_quantity') * data.get('item_price'))
