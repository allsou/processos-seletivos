import json
import logging

from connections.mongo import Mongo
from connections.redis import Redis
from models.user import User
from utils.validators import is_valid_id

LOGGER = logging.getLogger('sLogger')


class UserRepository:

    def __init__(self):
        """ Constructor """
        self.__mongo = Mongo()
        self.__redis = Redis().client

    def create_user(self, payload: dict):
        """

        Args:
            payload: body from request

        Returns: User

        """
        LOGGER.info('Creating user')
        user = User(
            **payload
        )
        user.save()
        self.__redis.set(str(user.id), 'created')
        return user

    def update_user_by_id(self, user_id: str, payload: dict):
        """

        Args:
            user_id: identification
            payload: request body

        Returns: User

        """
        LOGGER.info('Updating user')
        user = None
        if is_valid_id(user_id):
            query_set = User.objects(id=user_id)
            if query_set:
                user = query_set[0]
                user.populate(payload)
                user.save()
                self.__redis.set(str(user.id), 'updated')
        return user

    def delete_user_by_id(self, user_id: str):
        """

        Args:
            user_id: identification

        Returns: User

        """
        LOGGER.info('Deleting user')
        was_deleted = False
        if is_valid_id(user_id):
            query_set = User.objects(id=user_id)
            if query_set:
                query_set.delete()
                self.__redis.delete(str(user_id))
                was_deleted = True
        return was_deleted

    def get_user_by_id(self, user_id: str):
        """

        Args:
            user_id: identification

        Returns: User

        """
        LOGGER.info('Getting user')
        if is_valid_id(user_id):
            query_set = User.objects(id=user_id)
            if query_set:
                self.__redis.set(str(query_set[0].id), 'consulted')
                return query_set[0].to_response()

    def get_users(self, user_ids: list, view: str):
        """

        Args:
            user_ids: identification
            view: name to get from cache

        Returns:

        """
        LOGGER.info('Getting users')
        response = []
        ids = list(filter(lambda ident: is_valid_id(ident), user_ids))
        if ids:
            if view == 'cached':
                cached_ids = self.__redis.mget(ids)
                if all(cached_ids):
                    response = ids
                else:
                    users_consulted = User.objects(id__in=ids).fields(id=1)
                    response = self.__get_all_users_and_set_cache(users_consulted)
            else:
                response = json.loads(User.objects(id__in=ids).to_json())
        elif not ids and not user_ids and view == 'cached':
            users_consulted = User.objects.fields(id=1)
            response = self.__get_all_users_and_set_cache(users_consulted)
        elif not ids and not user_ids and not view:
            users_consulted = User.objects
            response = json.loads(users_consulted.to_json())
        return response

    def __get_all_users_and_set_cache(self, users_consulted):
        """

        Args:
            users_consulted: list of User

        Returns: List of parsed User

        """
        users_parse = []
        for index in range(0, len(users_consulted)):
            identification = json.loads(
                users_consulted[index].to_json()
            ).get('_id').get('$oid')
            users_parse.append(identification)
            self.__redis.set(identification, 'consulted')
        return users_parse
