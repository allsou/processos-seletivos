import logging
import os

from mongoengine import connect

LOGGER = logging.getLogger('sLogger')

# Service
SERVICE_PORT = os.environ.get('PORT', 8001)
SERVICE_HOST = os.environ.get('SERVICE_HOST', '0.0.0.0')

# Database
MONGO_DB_URL = os.environ.get('MONGO', 'mongodb://mongo:27017')
REDIS_URL = os.environ.get('REDIS', 'redis://redis:6379')
REDIS_TTL = int(os.environ.get('REDIS_TTL', 60 * 15))

# Withdraw
DAILY_LIMIT = float(os.environ.get('DAILY_LIMIT', 2000))


def connect_to_mongo_database():
    """ Open mongo connection """
    LOGGER.info('Connecting to mongo...')
    connect('dock', host=MONGO_DB_URL)
    LOGGER.info('Mongo connected!')


def initialize():
    """ Load initial data and connect to database """
    LOGGER.debug('Start setup')
    connect_to_mongo_database()
