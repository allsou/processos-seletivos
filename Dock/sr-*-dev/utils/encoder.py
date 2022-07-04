import json
from datetime import datetime

from bson.objectid import ObjectId


class Encoder(json.JSONEncoder):

    def default(self, obj):  # pylint: disable=E0202
        if isinstance(obj, datetime):
            return str(obj)
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)
