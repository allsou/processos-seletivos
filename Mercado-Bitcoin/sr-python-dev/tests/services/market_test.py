import unittest

import pytest

from connections.postgre import Postgre
from entities.market import Market
from services.markets import MarketService
from tests.fixtures.market_data import INSTANCE_MARKET_SUCCESS


class MarketServiceTest(unittest.TestCase):
    mocker = None

    @pytest.fixture(autouse=True)
    def __inject_fixtures(self, mocker):
        """ Injection of mock """
        self.mocker = mocker

    def setUp(self) -> None:
        self.mocker.patch.object(Postgre, '__init__', return_value=None)

    def test_get_market_by_registry_successfully(self):
        self.mocker.patch.object(Postgre, 'get_market_by_registry', return_value=Market(**INSTANCE_MARKET_SUCCESS))
        MarketService().get_market_by_registry('0000-00')

    def test_delete_market_successfully(self):
        self.mocker.patch.object(Postgre, 'delete_market_by_registry', return_value=None)
        MarketService().delete_market('0000-00')
