import json
import unittest
from datetime import datetime

from bson.objectid import ObjectId

from utils.encoder import Encoder


class EncoderTest(unittest.TestCase):
    def test_custom_encoder(self):
        """ Test encode of datetime and ObjeciId"""
        data = {
            'datetime': datetime.now(),
            'object_id': ObjectId('5f295dfc94055689412b05d4')
        }
        encoded_data = json.loads(json.dumps(data, cls=Encoder))

        self.assertTrue(isinstance(encoded_data.get('datetime'), str))
        self.assertTrue(isinstance(encoded_data.get('object_id'), str))
        self.assertEqual(
            encoded_data.get('datetime'),
            data.get('datetime').strftime('%Y-%m-%d %H:%M:%S.%f')
        )
        self.assertEqual(
            encoded_data.get('object_id'),
            str(data.get('object_id'))
        )
