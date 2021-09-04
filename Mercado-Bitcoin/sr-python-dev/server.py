import logging
from logging.config import fileConfig

import uvicorn
from starlette.applications import Starlette

import settings
from router import Router

fileConfig('logging_config.ini')
LOGGER = logging.getLogger('sLogger')


def main():
    app = Starlette(debug=True, routes=Router.get_routes())
    LOGGER.info(f'Market Service at {settings.SERVICE_HOST} listening {settings.SERVICE_PORT}')
    uvicorn.run(app, host=settings.SERVICE_HOST, port=settings.SERVICE_PORT)


if __name__ == '__main__':
    main()
