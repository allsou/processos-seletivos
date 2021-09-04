ARGS=market
MARKET=docker-compose -f docker-compose.yml
MARKET_DEV=-f docker-compose.dev.yml
DEV=true

build:
	$(MARKET) $(shell $(DEV) && echo $(MARKET_DEV)) build

coverage:
	$(MARKET) exec $(ARGS) pytest --cov-report html:cov_html --cov=./

migrate:
	docker exec -it $$(docker ps -q -f 'name=market') python migrations/feiras_csv_to_database.py

stop:
	docker stop $$(docker ps -q) || true

restart:
	$(MARKET) $(shell $(DEV) && echo $(MARKET_DEV)) restart $(ARGS)

test-unit:
	$(MARKET) $(shell $(DEV) && echo $(MARKET_DEV)) exec $(ARGS) pytest tests -vv

up:
	$(MARKET) $(shell $(DEV) && echo $(MARKET_DEV)) up -d $$ARGS

up-migrate: stop up migrate

watch:
	$(MARKET) $(shell $(DEV) && echo $(MARKET_DEV)) logs -f --tail=100 $(ARGS)