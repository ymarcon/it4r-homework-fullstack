install:
	npm install
	$(MAKE) -C backend install
	$(MAKE) -C frontend install

dev-backend:
	$(MAKE) -C backend dev

dev-frontend:
	$(MAKE) -C frontend dev

docker-build:
	docker compose build

docker-up:
	docker compose up
