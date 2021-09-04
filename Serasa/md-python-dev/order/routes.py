"""
HTTP routes loads
"""
from starlette.routing import Route

from actions.create_order import CreateOrderAction
from actions.delete_order import DeleteOrderAction
from actions.get_order import GetOrderAction
from actions.update_order import UpdateOrderAction


class Routes:
    """
    A class used to define Starlette routes

    Methods:
        get_routes -- Return a list of routes
    """

    @staticmethod
    def get_routes(base_path):
        """
        Method that returns routes with version appended

        Arguments:
            base_path {str} -- indicates the base path to append in every route

        Returns:
            [Routes] -- list of Route
        """
        return [
            Route(
                f'{base_path}/order',
                CreateOrderAction.create_order,
                methods=['POST']
            ),
            Route(
                f'{base_path}/order/' + '{order_id}',
                GetOrderAction.get_order,
                methods=['GET']
            ),
            Route(
                f'{base_path}/order/' + '{order_id}',
                DeleteOrderAction.delete_order,
                methods=['DELETE']
            ),
            Route(
                f'{base_path}/order/' + '{order_id}',
                UpdateOrderAction.update_order,
                methods=['PUT']
            ),
            Route(
                f'{base_path}/orders',
                GetOrderAction.get_orders,
                methods=['GET']
            )
        ]
