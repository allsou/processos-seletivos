stop-all:
	docker stop $$(docker ps -q) || true

build-and-up-project: build up

build:
	docker-compose build

up:
	docker-compose up -d

watch:
	docker-compose logs -f --tail=100

restart:
	docker-compose restart

unit-test: build-and-up-project
	docker-compose exec order pytest tests
	docker-compose exec user pytest tests
