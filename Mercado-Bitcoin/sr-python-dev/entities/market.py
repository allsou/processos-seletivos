from sqlalchemy import Column, Integer, BigInteger, String

from sqlalchemy.ext.declarative import declarative_base


class Market(declarative_base()):
    __tablename__ = 'markets'
    id = Column(Integer, primary_key=True)
    long = Column(Integer)
    lat = Column(Integer)
    setcens = Column(BigInteger)
    areap = Column(BigInteger)
    coddist = Column(Integer)
    distrito = Column(String)
    codsubpref = Column(Integer)
    subprefe = Column(String)
    regiao5 = Column(String)
    regiao8 = Column(String)
    nome_feira = Column(String)
    registro = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    bairro = Column(String)
    referencia = Column(String)
