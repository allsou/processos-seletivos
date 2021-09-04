from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from entities.market import Market
from exceptions.market import NotFoundException
from settings import LOGGER

engine = create_engine(
    f'postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@postgre:5432/{settings.DATABASE_NAME}'
)
Session = sessionmaker(bind=engine)


class Postgre:
    def __init__(self):
        self.session = Session()

    def get_market_by_registry(self, registry: str) -> Market:
        LOGGER.debug('Querying market by record')
        market = self.session.query(Market).filter(Market.registro == registry).first()
        if not market:
            raise NotFoundException
        return market

    def get_markets(self, query: str) -> list:
        LOGGER.debug('Querying markets')
        connection = engine.connect()
        if not query:
            select = f'SELECT * FROM markets'
        else:
            select = f'SELECT * FROM markets WHERE {query}'
        markets = connection.execute(select)
        return markets

    def insert_market(self, market: Market) -> Market:
        LOGGER.debug('Inserting market')
        self.session.add(market)
        self.session.commit()
        self.session.refresh(market)
        self.session.close()
        return market

    def delete_market_by_registry(self, registry: str):
        LOGGER.debug('Deleting market')
        market = self.get_market_by_registry(registry=registry)
        self.session.delete(market)
        self.session.commit()
        self.session.close()

    def update_market(self, market: Market, data: dict):
        LOGGER.debug('Updating market')
        for key, value in data.items():
            setattr(market, key, value)
        self.session.commit()
        self.session.refresh(market)
        self.session.close()
        return market
