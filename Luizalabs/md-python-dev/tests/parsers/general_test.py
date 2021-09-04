import unittest

from entities.customer import Customer
from parsers.general import Parser
from tests.fixtures.customer import CUSTOMER


class GeneralParserTest(unittest.TestCase):
    def test_parse_customer_favorites_successfully(self):
        customer = Customer(**CUSTOMER)
        data_parsed = Parser().parse_customer_favorites(customer=customer)
        self.assertEqual(customer.name, data_parsed.get('name'))
        self.assertEqual(customer.email, data_parsed.get('email'))
        self.assertEqual(customer.favorites, data_parsed.get('favorites'))

    def test_raw_to_json_successfully(self):
        customer = Customer(**CUSTOMER)
        Parser.raw_to_json(data=customer.to_mongo().to_dict())

    def test_raw_to_json_failure_incorrect_data(self):
        with self.assertRaises(Exception):
            customer = Customer(**CUSTOMER)
            Parser.raw_to_json(data=customer)

    def test_page_successfully_none(self):
        page = Parser.page(None)
        self.assertEqual(1, page)

    def test_page_successfully_valid_number(self):
        page = Parser.page('2')
        self.assertEqual(2, page)

    def test_page_failure_invalid_number(self):
        with self.assertRaises(Exception):
            Parser.page('2,a')
