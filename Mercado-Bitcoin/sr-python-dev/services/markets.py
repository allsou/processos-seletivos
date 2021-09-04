from connections.postgre import Postgre
from entities.market import Market
from parsers.market import MarketParser
from settings import LOGGER
from validations.market import MarketValidations


class MarketService:
    def __init__(self):
        self.validations = MarketValidations()
        self.database = Postgre()
        self.parser = MarketParser()

    def get_market_by_registry(self, registry: str):
        self.validations.is_valid_registry(registry=registry)
        LOGGER.debug(f'Getting maker by record {registry} service')
        market = self.database.get_market_by_registry(registry=registry)
        return self.parser.object_to_json(market=market)

    def create_market(self, data: dict):
        self.validations.new_market(data=data)
        self.validations.is_valid_registry(registry=data.get('registro'))
        LOGGER.debug('Creating new market service')
        new_market = Market(**data)
        market = self.database.insert_market(market=new_market)
        return self.parser.object_to_json(market=market)

    def delete_market(self, registry: str):
        self.validations.is_valid_registry(registry=registry)
        LOGGER.debug('Deleting market service')
        self.database.delete_market_by_registry(registry=registry)

    def get_markets(self, params: list):
        LOGGER.debug('Getting markets service')
        query = self.parser.params_to_query(params=params)
        markets = self.database.get_markets(query=query)
        return self.parser.markets_to_json(markets=markets)

    def update_market(self, data: dict, registry: str):
        self.validations.update_market(data=data)
        self.validations.is_valid_registry(registry=registry)
        LOGGER.debug('Updating new market service')
        market = self.database.get_market_by_registry(registry=registry)
        market = self.database.update_market(market=market, data=data)
        return self.parser.object_to_json(market=market)
