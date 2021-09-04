import unittest

from starlette.responses import JSONResponse

from utils.response_generator import generate_response


class MarketEntityTest(unittest.TestCase):
    def test_generate_response(self):
        response = generate_response()
        json = JSONResponse({
            "message": [],
            "notice": [],
            "data": {}
        }, status_code=200)
        self.assertEqual(response.body, json.body)
