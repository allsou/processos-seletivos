import bson


def is_valid_id(identification: str):
    """

    Args:
        identification: id in bson type

    Returns: Boolean

    """
    valid = False
    if identification and bson.objectid.ObjectId.is_valid(identification):
        valid = True
    return valid
