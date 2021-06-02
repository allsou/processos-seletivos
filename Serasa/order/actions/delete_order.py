"""
Action to delete order module
"""
import logging
import traceback

from peewee import IntegrityError

from serivces.order_repository import OrderRepository
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class DeleteOrderAction:
    @staticmethod
    async def delete_order(request):
        """
        Get order action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize delete order action.')
        try:
            order_id = request.path_params['order_id']
            if order_id:
                order = OrderRepository().delete_order(order_id)
                if order:
                    LOGGER.info('Order deleted successfully.')
                    return response(message='Order deleted', status_code=200)
            LOGGER.info('Order not found.')
            return response(message="Order not found", status_code=404)
        except (AttributeError, IntegrityError, TypeError):
            LOGGER.error(traceback.format_exc())
            return response(message="Invalid Payload", status_code=422)
        except Exception as error:
            LOGGER.debug(type(error))
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
