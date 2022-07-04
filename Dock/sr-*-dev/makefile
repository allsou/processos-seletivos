ARGS=dock
COMPOSE=docker-compose -f docker-compose.yml
COMPOSE_DEV=-f docker-compose.dev.yml
DEV=true

stop:
	docker stop $$(docker ps -q) || true

build:
	$(COMPOSE) $(shell $(DEV) && echo $(COMPOSE_DEV)) build

up:
	$(COMPOSE) $(shell $(DEV) && echo $(COMPOSE_DEV)) up -d

watch:
	$(COMPOSE) $(shell $(DEV) && echo $(COMPOSE_DEV)) logs -f --tail=100 $(ARGS)

test-unit:
	$(COMPOSE) $(shell $(DEV) && echo $(COMPOSE_DEV)) exec $(ARGS) pytest tests

restart:
	$(COMPOSE) $(shell $(DEV) && echo $(COMPOSE_DEV)) restart $(ARGS)