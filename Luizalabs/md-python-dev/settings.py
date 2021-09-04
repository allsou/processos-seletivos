import logging
import os

from mongoengine import connect

LOGGER = logging.getLogger('sLogger')

# Service
SERVICE_PORT = os.environ.get('PORT', 3001)
SERVICE_HOST = os.environ.get('SERVICE_HOST', '0.0.0.0')

# Database
MONGO_DB_URL = os.environ.get('MONGO', 'mongodb://mongo:27017')

# Auth
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN', 'auth0.com')
API_AUDIENCE = os.environ.get('API_AUDIENCE', 'http://localhost:3000')


def connect_to_mongo_database():
    """ Open mongo connection """
    LOGGER.info('Connecting to mongo...')
    connect('favorites', host=MONGO_DB_URL)
    LOGGER.info('Mongo connected!')


def initialize():
    """ Load initial data and connect to database """
    LOGGER.debug('Initiate setup')
    connect_to_mongo_database()
