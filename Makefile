# Makefile
init:
	docker-compose stop
	docker-compose build --no-cache
dev:
	docker-compose up
prod:
	docker-compose -f docker-compose.yml up
	# docker-compose -f docker-compose.yml up -d