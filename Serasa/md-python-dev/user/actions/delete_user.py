"""
Action to delete user module
"""
import logging
import traceback

from mongoengine import ValidationError

from services.user_repository import UserRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class DeleteUserAction:
    """ Delete action """
    @staticmethod
    async def delete_user(request):
        """
        Delete user action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize delete user action.')
        try:
            user_id = request.path_params['user_id']
            repository = UserRepository()
            if repository.delete_user_by_id(user_id):
                LOGGER.info('User deleted successfully.')
                return response(message="User deleted")
            LOGGER.info('User not found.')
            return response(message="User not found", status_code=404)

        except ValidationError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error, status_code=422)
        except TypeError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error, status_code=422)
        except Exception:
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
