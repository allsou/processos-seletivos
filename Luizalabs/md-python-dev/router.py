from starlette.routing import Route

from actions.customer import CustomerAction
from actions.product import ProductAction
from actions.favorites import FavoritesAction
BASE_PATH = '/api'
POST_METHOD = 'POST'
GET_METHOD = 'GET'
DELETE_METHOD = 'DELETE'
PATCH_METHOD = 'PATCH'
PUT_METHOD = 'PUT'


class Router:

    @staticmethod
    def get_routes():
        return [
            Route(f'{BASE_PATH}/product', ProductAction().create_product, methods=[POST_METHOD]),
            Route(f'{BASE_PATH}/product', ProductAction().get_products, methods=[GET_METHOD]),
            Route(f'{BASE_PATH}/product/{{product_id}}', ProductAction().get_product, methods=[GET_METHOD]),
            Route(f'{BASE_PATH}/product/{{product_id}}', ProductAction().delete_product, methods=[DELETE_METHOD]),
            Route(f'{BASE_PATH}/product/{{product_id}}', ProductAction().update_product, methods=[PATCH_METHOD]),
            Route(f'{BASE_PATH}/customer', CustomerAction().create_customer, methods=[POST_METHOD]),
            Route(f'{BASE_PATH}/customer/{{customer_id}}', CustomerAction().get_customer, methods=[GET_METHOD]),
            Route(f'{BASE_PATH}/customer/{{customer_id}}', CustomerAction().delete_customer, methods=[DELETE_METHOD]),
            Route(f'{BASE_PATH}/customer/{{customer_id}}', CustomerAction().update_customer, methods=[PATCH_METHOD]),
            Route(
                f'{BASE_PATH}/customer/{{customer_id}}/favorites/{{product_id}}',
                FavoritesAction().insert_favorite,
                methods=[PUT_METHOD]
            ),
            Route(
                f'{BASE_PATH}/customer/{{customer_id}}/favorites/{{product_id}}',
                FavoritesAction().remove_favorite,
                methods=[DELETE_METHOD]
            )
        ]
