from settings.base import LOGGER, REDIS_TTL

from .resources.redis import RedisConnection


class Cache:
    def __init__(self) -> None:
        self.__redis = RedisConnection()

    def get(self, key):
        LOGGER.debug(f'Getting data {key} at cache')
        return self.__redis.connection.get(key)

    def set(self, key, value):
        LOGGER.debug(f'Setting data {key} at cache')
        self.__redis.connection.set(key, value, ex=REDIS_TTL)
