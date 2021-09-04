"""
Settings data module
"""
import os

from dotenv import load_dotenv

load_dotenv()

# API
SERVICE_HOST = os.getenv('ORDER_SERVICE_HOST')
SERVICE_PORT = os.getenv('ORDER_SERVICE_PORT')

# MySQL
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_HOST = os.getenv('MYSQL_HOST')

# User API
USER_HOST = os.getenv('USER_HOST')

# Elasticsearch
ELASTIC_URL = os.getenv('ELASTIC_URL')
