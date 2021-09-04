import traceback
from json import JSONDecodeError

from sqlalchemy.exc import (
    IntegrityError,
    DataError
)

from exceptions.market import (
    InvalidRecordException,
    NotFoundException,
    MissingRequiredFieldsException
)
from services.markets import MarketService
from settings import LOGGER
from utils.messages import (
    CRITICAL_ERROR,
    INVALID_PAYLOAD,
    REGISTRY_ALREADY_USED,
    INVALID_FIELD_VALUE
)
from utils.response_generator import generate_response


class MarketsAction:
    def __init__(self):
        self.service = MarketService()

    async def create_market(self, request):
        try:
            LOGGER.debug('Creating market action')
            payload = await request.json()
            market = self.service.create_market(data=payload)
            return generate_response(data=market, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except InvalidRecordException as exception:
            LOGGER.debug("Invalid record param")
            return generate_response(message=exception.messages, status_code=422)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except DataError:
            LOGGER.debug("Invalid value informed")
            return generate_response(message=[INVALID_FIELD_VALUE], status_code=422)

        except IntegrityError:
            return generate_response(message=[REGISTRY_ALREADY_USED], status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def update_market(self, request):
        try:
            LOGGER.debug('Updating market action')
            registry = request.path_params.get('market_registry')
            payload = await request.json()
            market = self.service.update_market(registry=registry, data=payload)
            return generate_response(data=market, status_code=201)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except InvalidRecordException as exception:
            LOGGER.debug("Invalid record param")
            return generate_response(message=exception.messages, status_code=422)

        except MissingRequiredFieldsException as exception:
            return generate_response(message=exception.messages, status_code=400)

        except DataError:
            LOGGER.debug("Invalid value informed")
            return generate_response(message=[INVALID_FIELD_VALUE], status_code=422)

        except IntegrityError:
            return generate_response(message=[REGISTRY_ALREADY_USED], status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def get_market_by_registry(self, request):
        try:
            LOGGER.debug('Getting market action')
            record = request.path_params.get('market_registry')
            market = self.service.get_market_by_registry(registry=record)
            return generate_response(data=market, status_code=200)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except NotFoundException:
            LOGGER.debug('Market not found')
            return generate_response(status_code=404)

        except InvalidRecordException as exception:
            LOGGER.debug("Invalid record param")
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def delete_market(self, request):
        try:
            LOGGER.debug('Deleting market action')
            record = request.path_params.get('market_registry')
            market = self.service.delete_market(registry=record)
            return generate_response(data=market, status_code=200)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except NotFoundException:
            LOGGER.debug('Market not found')
            return generate_response(status_code=404)

        except InvalidRecordException as exception:
            LOGGER.debug("Invalid record param")
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])

    async def get_markets(self, request):
        try:
            LOGGER.debug('Getting markets action')
            params = request.query_params.multi_items()
            markets = self.service.get_markets(params=params)
            return generate_response(data=markets, status_code=200)

        except JSONDecodeError:
            LOGGER.debug("Invalid payload")
            return generate_response(message=[INVALID_PAYLOAD], status_code=400)

        except NotFoundException:
            LOGGER.debug('Market not found')
            return generate_response(status_code=404)

        except InvalidRecordException as exception:
            LOGGER.debug("Invalid record param")
            return generate_response(message=exception.messages, status_code=422)

        except Exception as exception:
            LOGGER.debug(traceback.format_exc())
            LOGGER.critical(f"Unknown error: {exception}")
            return generate_response(status_code=500, message=[CRITICAL_ERROR])