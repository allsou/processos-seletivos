from redis import Redis

from settings.base import REDIS_URL


class RedisConnection:
    def __init__(self) -> None:
        self.connection = Redis.from_url(REDIS_URL)
