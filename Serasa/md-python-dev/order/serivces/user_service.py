import json
import logging
import traceback

import requests

import settings

LOGGER = logging.getLogger('sLogger')


def get_user(user_id: str):
    """

    Args:
        user_id: identification

    Returns: Response

    """
    LOGGER.info('Requesting user API')
    try:
        response = requests.get(
            settings.USER_HOST + '/v1/users',
            params={
                'user_id': user_id,
                'view': 'cached'
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
