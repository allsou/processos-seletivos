"""
Action to delete user module
"""
import logging
import traceback

from mongoengine.errors import ValidationError

from services.user_repository import UserRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class UpdateUserAction:
    """ Update Action """
    @staticmethod
    async def update_user(request):
        """
        Update user action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize update user action.')
        try:
            user_id = request.path_params['user_id']
            payload = await request.json()
            user = UserRepository().update_user_by_id(user_id, payload)
            if user:
                LOGGER.info('User updated successfully.')
                return response(data=user.to_response(), status_code=200)
            LOGGER.info('User not found.')
            return response(message="User not found", status_code=404)

        except ValidationError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error.message, status_code=422)
        except TypeError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error, status_code=422)
        except Exception:
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
