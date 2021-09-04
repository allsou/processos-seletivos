import unittest

from entities.market import Market
from tests.fixtures.market_data import INSTANCE_MARKET_SUCCESS


class MarketEntityTest(unittest.TestCase):
    def test_market_instance_successfully(self):
        Market(**INSTANCE_MARKET_SUCCESS)

    def test_market_instance_failure_with_invalid_field(self):
        with self.assertRaises(TypeError):
            Market(**{"fsafdsa": "fdasfdsa"})
