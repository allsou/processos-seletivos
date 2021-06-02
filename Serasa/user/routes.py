"""
HTTP routes loads
"""
from starlette.routing import Route

from actions.create_user import CreateUserAction
from actions.delete_user import DeleteUserAction
from actions.get_user import GetUserAction
from actions.get_users import GetUsersAction
from actions.update_user import UpdateUserAction


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
                f'{base_path}/user',
                CreateUserAction.create_user,
                methods=['POST']
            ),
            Route(
                f'{base_path}/user/' + '{user_id}',
                GetUserAction.get_user,
                methods=['GET']
            ),
            Route(
                f'{base_path}/user/' + '{user_id}',
                DeleteUserAction.delete_user,
                methods=['DELETE']
            ),
            Route(
                f'{base_path}/user/' + '{user_id}',
                UpdateUserAction.update_user,
                methods=['PUT']
            ),
            Route(
                f'{base_path}/users',
                GetUsersAction.get_users,
                methods=['GET']
            )
        ]
