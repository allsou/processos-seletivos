import json
import logging
import traceback

import requests

import settings

LOGGER = logging.getLogger('sLogger')


def make_search(item_description: str):
    """

    Args:
        item_description: description of item in order

    Returns: Response

    """
    LOGGER.info('Requesting elasticsearch')
    try:
        response = requests.get(
            settings.ELASTIC_URL + '/orders/order/_search',
            params={
                'q': item_description
            }
        )
        if response.status_code > 299:
            return None
        return json.loads(response.text)
    except requests.exceptions.HTTPError:
        LOGGER.error(traceback.format_exc())
    except requests.exceptions.ConnectionError:
        LOGGER.error(traceback.format_exc())
    except requests.exceptions.Timeout:
        LOGGER.error(traceback.format_exc())
    except Exception:
        LOGGER.error(traceback.format_exc())
