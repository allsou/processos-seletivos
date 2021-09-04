"""
Action to create user module
"""
import logging
import traceback

from mongoengine import ValidationError, NotUniqueError

from services.user_repository import UserRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class CreateUserAction:

    @staticmethod
    async def create_user(request):
        """
        Create user action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize create user action.')
        try:
            payload = await request.json()
            repository = UserRepository()
            user = repository.create_user(payload)
            LOGGER.info('User created successfully.')
            return response(data=user.to_response(), status_code=201)

        except ValidationError as error:
            LOGGER.error(traceback.format_exc())
            return response(message=error.to_dict(), status_code=422)
        except NotUniqueError:
            LOGGER.error(traceback.format_exc())
            return response(message="User already created", status_code=422)
        except Exception:
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
