ARGS=favorites
FAVORITES=docker-compose -f docker-compose.yml
FAVORITES_DEV=-f docker-compose.dev.yml
DEV=true

stop:
	docker stop $$(docker ps -q) || true

build:
	$(FAVORITES) $(shell $(DEV) && echo $(FAVORITES_DEV)) build

up:
	$(FAVORITES) $(shell $(DEV) && echo $(FAVORITES_DEV)) up -d

watch:
	$(FAVORITES) $(shell $(DEV) && echo $(FAVORITES_DEV)) logs -f --tail=100 $(ARGS)

restart:
	$(FAVORITES) $(shell $(DEV) && echo $(FAVORITES_DEV)) restart $(ARGS)

test-unit:
	$(FAVORITES) $(shell $(DEV) && echo $(FAVORITES_DEV)) exec $(ARGS) pytest tests