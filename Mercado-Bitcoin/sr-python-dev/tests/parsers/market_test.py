import unittest

from entities.market import Market
from parsers.market import MarketParser, DISTINCT_NUMBERS
from tests.fixtures.market_data import INSTANCE_MARKET_SUCCESS


class MarketParserTest(unittest.TestCase):
    def test_number_from_csv_to_int_without_number_successfully(self):
        number = MarketParser.number_from_csv_to_int('')
        self.assertEqual(number, 'S/N')

    def test_number_from_csv_to_int_distinct_number_successfully(self):
        for number in DISTINCT_NUMBERS:
            parsed_number = MarketParser.number_from_csv_to_int(number)
            self.assertEqual(parsed_number, number)

    def test_number_from_csv_to_int_successfully(self):
        number = MarketParser.number_from_csv_to_int('666.000')
        self.assertEqual(number, '666')

    def test_params_to_query_failure_raise_exception(self):
        with self.assertRaises(Exception):
            MarketParser.params_to_query(params=[1, 2, 3, 4, 5])

    def test_params_to_query_return_empty_string(self):
        query = MarketParser.params_to_query(params=[('pudim', 1)])
        self.assertEqual(query, '')

    def test_params_to_query_return_distrito(self):
        query = MarketParser.params_to_query(params=[('distrito', 1)])
        self.assertEqual(query, '"distrito" = \'1\'')

    def test_params_to_query_return_regiao5(self):
        query = MarketParser.params_to_query(params=[('regiao5', 1)])
        self.assertEqual(query, '"regiao5" = \'1\'')

    def test_params_to_query_return_nome_feira(self):
        query = MarketParser.params_to_query(params=[('nome_feira', 1)])
        self.assertEqual(query, '"nome_feira" = \'1\'')

    def test_params_to_query_return_bairro(self):
        query = MarketParser.params_to_query(params=[('bairro', 1)])
        self.assertEqual(query, '"bairro" = \'1\'')

    def test_object_to_json(self):
        market = Market(**INSTANCE_MARKET_SUCCESS)
        market_dict = MarketParser.object_to_json(market=market)
        self.assertEqual(market.id, market_dict.get('id'))

    def test_markets_to_json(self):
        market = list(INSTANCE_MARKET_SUCCESS.values())
        markets = [market]
        market_list = MarketParser.markets_to_json(markets=markets)
        self.assertEqual(market[0], market_list[0].get('id'))
