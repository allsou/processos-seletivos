import logging

from dotenv import dotenv_values

config = dotenv_values(".env")
LOGGER = logging.getLogger('sLogger')

# Service
SERVICE_PORT = config.get('MARKET_PORT', 3100)
SERVICE_HOST = config.get('MARKET_HOST', '0.0.0.0')

# Database - Postgre
DATABASE_USER = config.get('DATABASE_USER', 'market')
DATABASE_PASSWORD = config.get('DATABASE_PASSWORD', 'market')
DATABASE_NAME = config.get('DATABASE_NAME', 'market')
TABLE_NAME = 'markets'
