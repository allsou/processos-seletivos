# Approved?
![](https://github.com/allsou/ProcessosSeletivos/blob/master/assets/cancel.png)

# Market
Service responsible to manage markets.

## Prerequisites
These must be installed to run the application.
* [makefile](https://makefiletutorial.com/)
* [Docker](https://docs.docker.com/install/)
* [Docker-compose](https://docs.docker.com/compose/install/)

## Build
To build the project, you will need to type `make build`, after this you can run anothers commands on the project.
This will download docker images such as python and postgre.
> $ make build
```python
...
Step 10/10 : ENTRYPOINT python server.py
 ---> Running in e34d1d7cbf7d
Removing intermediate container e34d1d7cbf7d
 ---> b294055c3f80
Successfully built b294055c3f80
Successfully tagged mercado-bitcoin_market:latest
```

## Up services
Will start services or update.
> $ make up
```python
...
Recreating mercado-bitcoin_market_1 ... 
Recreating mercado-bitcoin_market_1 ... done
```

## Watch logs
To see logs registered at console.
> $ make watch
```python
...
market_1   | server.py [main] #[16] - INFO - Market Service at 0.0.0.0 listening 3100
market_1   | markets.py [create_market] #[31] - DEBUG - Creating market action
market_1   | market.py [new_market] #[42] - DEBUG - Validating create data
market_1   | markets.py [create_market] #[23] - DEBUG - Creating new market service
market_1   | postgre.py [insert_market] #[37] - DEBUG - Inserting market
```

## Shortcut
Build, up and watch services.
> $ make build up watch

## API Usage
### Request Collections
If necessary, all requests are already setup at a [Postman](https://www.postman.com/) collection in docs directory
- [./docs/Markets.postman_collection.json](https://github.com/allsou/mercado-bitcoin/blob/develop/docs/Markets.postman_collection.json)

### Requesting API
The requests can be done using the token and payload specified at requests collections
```python
curl --location --request POST 'http://localhost:3100/markets/v0/market' \
--header 'Content-Type: application/json' \
--data-raw '{
    "long": "-46550164",
    "lat": -23558733,
    "setcens": 355030885000091,
    "areap": 3550308005040,
    "coddist": 87,
    "distrito": "VILA FORMOSA",
    "codsubpref": 26,
    "subprefe": "ARICANDUVA-FORMOSA-CARRAO",
    "regiao5": "Leste",
    "regiao8": "Leste 1",
    "nome_feira": "VILA FORMOSA",
    "registro": "4430-0",
    "logradouro": "RUA MARAGOJIPE",
    "numero": "S/N",
    "bairro": "VL FORMOSA",
    "referencia": "TV RUA PRETORIA"
}'
```

```python
curl --location --request GET 'http://localhost:3100/markets/v0/markets?regiao5=Leste&bairro=BRAS' \
--header 'Content-Type: application/json' \
--data-raw '{}'
```

```python
curl --location --request PATCH 'http://localhost:3100/markets/v0/markets/4038-0' \
--header 'Content-Type: application/json' \
--data-raw '{
    "distrito": "LAPA",
    "regisro": "0000-0",
    "logradouro": "RUA TESTE"
}'
```
### Populate database
To migrate data from csv file to Postgre
> $ make migrate

## Tests
### unit
In this option you will run only lint and unit tests.
> $ make test-unit
```python
============================== test session starts ===============================
platform linux -- Python 3.7.11, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /app
plugins: anyio-3.3.0, mock-3.6.1, cov-2.12.1
collected 21 items                                                               

tests/entities/market_test.py::MarketEntityTest::test_market_instance_failure_with_invalid_field PASSED [  4%]
tests/entities/market_test.py::MarketEntityTest::test_market_instance_successfully PASSED [  9%]
tests/parsers/market_test.py::MarketParserTest::test_markets_to_json PASSED [ 14%]
tests/parsers/market_test.py::MarketParserTest::test_number_from_csv_to_int_distinct_number_successfully PASSED [ 19%]
tests/parsers/market_test.py::MarketParserTest::test_number_from_csv_to_int_successfully PASSED [ 23%]
tests/parsers/market_test.py::MarketParserTest::test_number_from_csv_to_int_without_number_successfully PASSED [ 28%]
tests/parsers/market_test.py::MarketParserTest::test_object_to_json PASSED [ 33%]
tests/parsers/market_test.py::MarketParserTest::test_params_to_query_failure_raise_exception PASSED [ 38%]
tests/parsers/market_test.py::MarketParserTest::test_params_to_query_return_bairro PASSED [ 42%]
tests/parsers/market_test.py::MarketParserTest::test_params_to_query_return_distrito PASSED [ 47%]
tests/parsers/market_test.py::MarketParserTest::test_params_to_query_return_empty_string PASSED [ 52%]
tests/parsers/market_test.py::MarketParserTest::test_params_to_query_return_nome_feira PASSED [ 57%]
tests/parsers/market_test.py::MarketParserTest::test_params_to_query_return_regiao5 PASSED [ 61%]
tests/services/market_test.py::MarketServiceTest::test_delete_market_successfully PASSED [ 66%]
tests/services/market_test.py::MarketServiceTest::test_get_market_by_registry_successfully PASSED [ 71%]
tests/utils/response_generator_test.py::MarketEntityTest::test_generate_response PASSED [ 76%]
tests/validations/market_test.py::MarketValidationsTest::test_is_valid_registry PASSED [ 80%]
tests/validations/market_test.py::MarketValidationsTest::test_is_valid_registry_failure_raise_exception PASSED [ 85%]
tests/validations/market_test.py::MarketValidationsTest::test_new_market PASSED [ 90%]
tests/validations/market_test.py::MarketValidationsTest::test_new_market_raise_exception PASSED [ 95%]
tests/validations/market_test.py::MarketValidationsTest::test_update_market PASSED [100%]

=============================== 21 passed in 0.26s ===============================

```
### coverage
In this option you will run only coverage of unit tests.
> $ make coverage
```python
================================== test session starts =================================
platform linux -- Python 3.7.11, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /app
plugins: anyio-3.3.0, mock-3.6.1, cov-2.12.1
collected 21 items                                                                   

tests/entities/market_test.py ..                                               [  9%]
tests/parsers/market_test.py ...........                                       [ 61%]
tests/services/market_test.py ..                                               [ 71%]
tests/utils/response_generator_test.py .                                       [ 76%]
tests/validations/market_test.py .....                                         [100%]

---------- coverage: platform linux, python 3.7.11-final-0 -----------
Coverage HTML written to dir cov_html


================================= 21 passed in 0.45s =================================
```
The coverage % can be seen at [.cov_html/index.html](https://github.com/allsou/mercado-bitcoin/blob/develop/cov_html/index.html)

# Made using
- [Mongoengine](http://mongoengine.org/) - ORM  
- [Pipenv](https://pipenv.pypa.io/en/latest/) - Dependencies manager
- [psycopg2-binary](https://www.psycopg.org/) - Database Adapter
- [Pytest](https://docs.pytest.org/en/latest) - Test Framework  
- [python-jose](https://github.com/mpdavis/python-jose) - JWT
- [sqlalchemy](https://www.sqlalchemy.org/) - ORM
- [Starlette](https://www.starlette.io) - Framework/Toolkit
- [Uvicorn](https://www.uvicorn.org) - ASGI server