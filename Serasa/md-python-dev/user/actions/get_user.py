"""
Action to get user module
"""
import logging
import traceback

from mongoengine import ValidationError

from services.user_repository import UserRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class GetUserAction:

    @staticmethod
    async def get_user(request):
        """
        Get user action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize get user action.')
        try:
            user_id = request.path_params['user_id']
            if user_id:
                user = UserRepository().get_user_by_id(user_id)
                if user:
                    LOGGER.info('User found successfully.')
                    return response(data=user, status_code=200)
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
