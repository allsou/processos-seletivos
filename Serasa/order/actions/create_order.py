"""

"""
import logging
import traceback

from peewee import IntegrityError

from serivces.order_repository import OrderRepository, UserException
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class CreateOrderAction:

    @staticmethod
    async def create_order(request):
        """
        Create order action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize create order action.')
        try:
            payload = await request.json()
            repository = OrderRepository()
            order = repository.create_order(payload)
            LOGGER.info(order)
            if order:
                LOGGER.info('Order created successfully.')
                return response(data=order, status_code=201)
        except UserException as error:
            return response(message=error.message, status_code=422)
        except (AttributeError, IntegrityError, TypeError):
            LOGGER.error(traceback.format_exc())
            return response(message="Invalid Payload", status_code=422)
        except Exception as error:
            LOGGER.info(type(error))
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
