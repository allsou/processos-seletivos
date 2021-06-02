"""
Action to get order module
"""
import logging
import traceback

from peewee import IntegrityError

from serivces.order_repository import OrderRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class GetOrderAction:
    @staticmethod
    async def get_order(request):
        """
        Get order action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize get order action.')
        try:
            order_id = request.path_params['order_id']
            if order_id:
                order = OrderRepository().get_order(order_id)
                if order:
                    LOGGER.info('Order found successfully.')
                    return response(data=order, status_code=200)
            LOGGER.info('Order not found.')
            return response(message="Order not found", status_code=404)
        except (AttributeError, IntegrityError, TypeError):
            LOGGER.error(traceback.format_exc())
            return response(message="Invalid Payload", status_code=422)
        except Exception as error:
            LOGGER.debug(type(error))
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)

    @staticmethod
    async def get_orders(request):
        """
        Get orders action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize get orders action.')
        try:
            query = request.query_params
            query_filtered = {
                'order_id': query.getlist('order_id'),
                'item_description': query.get('item_description')
            }
            orders = OrderRepository().get_orders(query_filtered)
            return response(data=orders, status_code=200)
        except (AttributeError, IntegrityError, TypeError, ValueError):
            LOGGER.error(traceback.format_exc())
            return response(message="Invalid Payload", status_code=422)
        except Exception as error:
            LOGGER.debug(type(error))
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)