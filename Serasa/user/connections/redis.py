"""
Database cache connection
"""
import redis
import settings


class Redis:

    def __init__(self):
        self.client = redis.from_url(settings.REDIS_URL)
