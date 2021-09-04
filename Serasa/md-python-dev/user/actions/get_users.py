"""
Action to get users module
"""
import logging
import traceback

from mongoengine import ValidationError

from services.user_repository import UserRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class GetUsersAction:

    @staticmethod
    async def get_users(request):
        """
        Get users action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize get users action.')
        try:
            query = request.query_params
            users = UserRepository().get_users(
                user_ids=query.getlist('user_id'),
                view=query.get('view')
            )
            return response(data=users, status_code=200)

        except ValidationError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error, status_code=422)
        except TypeError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error, status_code=422)
        except Exception:
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
