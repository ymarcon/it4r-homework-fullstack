install:
	npm install
	$(MAKE) -C backend install
	$(MAKE) -C frontend install

dev-backend:
	$(MAKE) -C backend dev

dev-frontend:
	$(MAKE) -C frontend dev
