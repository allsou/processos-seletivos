"""
Mongo connection module
"""
from mongoengine import connect
import settings


class Mongo:
    def __init__(self):
        """ Initialize mongo connection """
        self.connection = connect(
            'users',
            host=settings.MONGO_HOST
        )
