from starlette.routing import Route

from actions.markets import MarketsAction

BASE_PATH = '/markets/v0'
POST_METHOD = 'POST'
GET_METHOD = 'GET'
DELETE_METHOD = 'DELETE'
PATCH_METHOD = 'PATCH'


class Router:

    @staticmethod
    def get_routes():
        return [
            Route(f'{BASE_PATH}/market', MarketsAction().create_market, methods=[POST_METHOD]),
            Route(f'{BASE_PATH}/markets', MarketsAction().get_markets, methods=[GET_METHOD]),
            Route(
                f'{BASE_PATH}/markets/{{market_registry}}', MarketsAction().get_market_by_registry, methods=[GET_METHOD]
            ),
            Route(f'{BASE_PATH}/markets/{{market_registry}}', MarketsAction().delete_market, methods=[DELETE_METHOD]),
            Route(f'{BASE_PATH}/markets/{{market_registry}}', MarketsAction().update_market, methods=[PATCH_METHOD])
        ]
