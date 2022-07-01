import logging
from logging.config import fileConfig

import uvicorn
from starlette.applications import Starlette

import settings.base as base
from router import Router

fileConfig('settings/logging_config.ini')
LOGGER = logging.getLogger('sLogger')
app = Starlette(debug=True, routes=Router.get_routes())


def factory_run():
    base.initialize()
    LOGGER.info(
        f'Dock Service on {base.SERVICE_HOST} port {base.SERVICE_PORT}'
    )
    return app


def cli_run():
    LOGGER.info(
        f'Dock Service on {base.SERVICE_HOST} port {base.SERVICE_PORT}'
    )
    uvicorn.run(app, host='0.0.0.0', port='8001')


if __name__ == '__main__':
    base.initialize()
    cli_run()
