import json

from starlette.responses import JSONResponse
from starlette.routing import Route

from actions.account import AccountAction
from actions.holder import HolderAction

BASE_PATH = '/api/v0'
POST_METHOD = 'POST'
GET_METHOD = 'GET'
DELETE_METHOD = 'DELETE'
PUT_METHOD = 'PUT'


def openapi_schema(request):
    """Load API DOCS"""
    file = open('docs/swagger.json', 'r')
    return JSONResponse(json.loads(file.read()))


class Router:

    @staticmethod
    def get_routes():
        return [
            Route(
                f'{BASE_PATH}/holders',
                HolderAction().create,
                methods=[POST_METHOD]
            ),
            Route(
                f'{BASE_PATH}/holders/{{tax_id}}',
                HolderAction().delete,
                methods=[DELETE_METHOD]
            ),
            Route(
                f'{BASE_PATH}/accounts',
                AccountAction().create_account,
                methods=[POST_METHOD]
            ),
            Route(
                f'{BASE_PATH}/accounts/{{agency}}/{{number}}/active',
                AccountAction().change_account_active_status,
                methods=[PUT_METHOD]
            ),
            Route(
                f'{BASE_PATH}/accounts/{{agency}}/{{number}}/blocked',
                AccountAction().change_account_block_status,
                methods=[PUT_METHOD]
            ),
            Route(
                f'{BASE_PATH}/accounts/{{agency}}/{{number}}/transactions',
                AccountAction().create_transaction, methods=[POST_METHOD]
            ),
            Route(
                f'{BASE_PATH}/accounts/{{agency}}/{{number}}/transactions',
                AccountAction().get_transactions, methods=[GET_METHOD]
            ),
            Route(
                f'{BASE_PATH}/accounts/{{agency}}/{{number}}/balance',
                AccountAction().get_balance, methods=[GET_METHOD]
            ),
            Route(f'{BASE_PATH}/docs', openapi_schema, methods=[GET_METHOD])
        ]
