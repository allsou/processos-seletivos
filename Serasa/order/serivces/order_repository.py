import json
import logging
import traceback
from datetime import datetime

from peewee import OperationalError
from playhouse.shortcuts import model_to_dict

from connections.mysql import Mysql
from entities.order import Order
from serivces.elasticsearch_service import make_search
from serivces.user_service import get_user

LOGGER = logging.getLogger('sLogger')


class OrderRepository:
    def __init__(self):
        try:
            self.__connection = Mysql().database.connect()
            Order.create_table()
        except OperationalError:
            LOGGER.error(traceback.format_exc())

    def create_order(self, payload: dict):
        """

        Args:
            payload: request body

        Returns: Order

        """
        LOGGER.info('Creating an order')
        if payload.get('user_id'):
            self.is_user_valid(payload.get('user_id'))
            order = Order.create(
                user_id=payload.get('user_id'),
                item_description=payload.get('item_description'),
                item_quantity=payload.get('item_quantity'),
                item_price=payload.get('item_price'),
                total_value=(payload.get('item_quantity') * payload.get('item_price'))
            )
            return self.parse_to_json(order)

    def get_order(self, order_id: int):
        """

        Args:
            order_id: identification

        Returns: Order

        """
        LOGGER.info('Getting an order')
        order = {}
        try:
            order = Order.get_by_id(order_id)
        except Exception:
            return order
        if order:
            order = self.parse_to_json(order)
        return order

    def update_order(self, order_id: int, payload: dict):
        """

        Args:
            order_id: identification
            payload: request body

        Returns:

        """
        LOGGER.info('Updating order')
        order = {}
        try:
            order = Order.get_by_id(order_id)
            if payload.get('user_id'):
                self.is_user_valid(payload.get('user_id'))
            order.user_id = payload.get('user_id', order.user_id)
            order.item_description = payload.get('item_description', order.item_description)
            order.item_quantity = payload.get('item_quantity', order.item_quantity)
            order.item_price = payload.get('item_price', order.item_price)
            order.updated_at = datetime.now()
            updated_rows = order.save()
        except UserException as error:
            raise error
        except Exception:
            return order
        if updated_rows:
            order = self.parse_to_json(order)
        return order

    @staticmethod
    def delete_order(order_id: int):
        """

        Args:
            order_id: identification

        Returns: Response

        """
        LOGGER.info('Deleting an order')
        was_deleted = False
        order = Order.delete_by_id(order_id)
        if order:
            was_deleted = True
        return was_deleted

    def get_orders(self, query: dict):
        """

        Args:
            query: request query params

        Returns: Order list

        """
        LOGGER.info('Getting orders')
        orders = []
        if not query.get('order_id') and not query.get('item_description'):
            orders = Order.select().execute()
            orders = [self.parse_to_json(order) for order in orders]
        elif query.get('order_id') and not query.get('item_description'):
            ids_to_query = [int(identify) for identify in query.get('order_id')]
            orders = Order.select().where(Order.id.in_(ids_to_query))
            orders = [self.parse_to_json(order) for order in orders]
        elif not query.get('order_id') and query.get('item_description'):
            orders = make_search(query.get('item_description'))
            orders = orders.get('hits').get('hits')
        return orders

    @staticmethod
    def parse_to_json(order: Order):
        return json.loads(json.dumps(
            model_to_dict(order),
            default=lambda value: str(value) if isinstance(value, datetime) else value
        ))

    @staticmethod
    def is_user_valid(user_id: str):
        user = get_user(user_id)
        if not user.get('data'):
            raise UserException('Invalid user')


class UserException(Exception):
    """"""

    def __init__(self, message: str):
        self.message = message
