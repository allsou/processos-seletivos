import unittest

from tests.fixtures.market_data import INSTANCE_MARKET_SUCCESS
from validations.market import MarketValidations


class MarketValidationsTest(unittest.TestCase):
    def test_is_valid_registry(self):
        self.assertIsNone(
            MarketValidations.is_valid_registry('0000-0')
        )

    def test_is_valid_registry_failure_raise_exception(self):
        with self.assertRaises(Exception):
            MarketValidations.is_valid_registry('0000-')

    def test_new_market(self):
        temp_dict = INSTANCE_MARKET_SUCCESS.copy()
        MarketValidations().new_market(temp_dict)
        without_id = INSTANCE_MARKET_SUCCESS.copy()
        del without_id['id']
        self.assertEqual(temp_dict, without_id)

    def test_new_market_raise_exception(self):
        with self.assertRaises(Exception):
            MarketValidations().new_market({})

    def test_update_market(self):
        temp_dict = INSTANCE_MARKET_SUCCESS.copy()
        del temp_dict['registro']
        MarketValidations().update_market(temp_dict)
        without_id = INSTANCE_MARKET_SUCCESS.copy()
        del without_id['id']
        del without_id['registro']

        self.assertEqual(temp_dict, without_id)
