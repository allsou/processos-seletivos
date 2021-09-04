import bson

from exceptions.general import NotFoundException
from settings import LOGGER


def is_object_id(object_id: str):
    LOGGER.debug(f'Validating id {object_id}')
    if not bson.objectid.ObjectId.is_valid(object_id):
        LOGGER.debug('Invalid id informed')
        raise NotFoundException
