"""
Settings data module
"""
import os

from dotenv import load_dotenv

load_dotenv()

# Service
SERVICE_HOST = os.getenv('USER_SERVICE_HOST')
SERVICE_PORT = os.getenv('USER_SERVICE_PORT')
# Mongo
MONGO_HOST = os.getenv('MONGO_HOST')
# Redis
REDIS_URL = os.getenv('REDIS_URL')
