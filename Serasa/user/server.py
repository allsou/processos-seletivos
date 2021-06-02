"""
Main module
"""
import logging
from logging.config import fileConfig

import uvicorn
from starlette.applications import Starlette

import settings
from routes import Routes

fileConfig('configs/logging_config.ini')
LOGGER = logging.getLogger('sLogger')
BASE_PATH = '/v1'  # Software Version

if __name__ == "__main__":
    LOGGER.info('Initialize service')
    app = Starlette(routes=Routes.get_routes(BASE_PATH))
    LOGGER.debug(f'Server up {settings.SERVICE_HOST} at port {settings.SERVICE_PORT}')
    uvicorn.run(app, host=settings.SERVICE_HOST, port=int(settings.SERVICE_PORT))
