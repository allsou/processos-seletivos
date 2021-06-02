"""
Database Connection
"""
from peewee import MySQLDatabase

import settings


class Mysql:
    def __init__(self):
        self.database = MySQLDatabase('order', user=settings.MYSQL_USER, password=settings.MYSQL_PASSWORD,
                                      host=settings.MYSQL_HOST)
