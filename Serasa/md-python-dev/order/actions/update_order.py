"""
Action to update order module
"""
import logging
import traceback

from peewee import IntegrityError

from serivces.order_repository import OrderRepository, UserException
from utils.response_generator import response

LOGGER = logging.getLogger('sLogger')


class UpdateOrderAction:
    @staticmethod
    async def update_order(request):
        """
        Update order action
        :param request: Request
        :return: Response
        """
        LOGGER.info('Initialize update order action.')
        try:
            order_id = request.path_params['order_id']
            payload = await request.json()
            if order_id:
                order = OrderRepository().update_order(order_id, payload)
                if order:
                    LOGGER.info('Order updated successfully.')
                    return response(data=order, status_code=200)
            LOGGER.info('Order not found.')
            return response(message="Order not found", status_code=404)
        except UserException as error:
            return response(message=error.message, status_code=422)
        except (AttributeError, IntegrityError, TypeError):
            LOGGER.error(traceback.format_exc())
            return response(message="Invalid Payload", status_code=422)
        except Exception as error:
            LOGGER.debug(type(error))
            LOGGER.critical(traceback.format_exc())
            return response(message="Unknown error", status_code=500)
