import json

from connections.database import LIMIT_PER_PAGE
from exceptions.general import InvalidParamValueException
from utils.encoder import Encoder


class Parser:

    def parse_customer_favorites(self, customer):
        favorites = []
        for favorite in customer.favorites:
            favorites.append(favorite.to_mongo().to_dict())
        customer_dict = customer.to_mongo().to_dict()
        customer_dict['favorites'] = favorites
        return self.raw_to_json(data=customer_dict)

    @staticmethod
    def raw_to_json(data: dict) -> dict:
        parsed_data = json.dumps(data, cls=Encoder)
        return json.loads(parsed_data)

    @staticmethod
    def page(page: str) -> int:
        try:
            if not page:
                page_parsed = 1
            else:
                page_parsed = int(page)
            return page_parsed
        except Exception:
            raise InvalidParamValueException(param='page')

    @staticmethod
    def products(data: list, total: int, page: int):
        parsed_data = json.dumps(data, cls=Encoder)
        next_page = page + 1
        previous_page = page - 1
        return {
            'total': total,
            'page': page,
            'items': len(data),
            'previous_page': previous_page if previous_page != 0 else None,
            'next_page': next_page if len(data) == LIMIT_PER_PAGE else None,
            'products': json.loads(parsed_data)
        }
