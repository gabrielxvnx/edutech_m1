#makefile
PHONY: setup docker-up docker-down docker-logs create-schema insert-data run-queries generate-data validate-csv process-reports clean

# Setup
setup: docker-up create-schema insert-data

# Docker
docker-up:
	docker-compose up -d

docker-down:
	docker-compose down

docker-logs:
	docker-compose logs -f postgres

# Database
create-schema:
	docker exec -i edutech_postgres psql -U edutech_user -d edutech < sql/schema.sql

insert-data:
	docker exec -i edutech_postgres psql -U edutech_user -d edutech < sql/dados.sql

run-queries:
	docker exec -i edutech_postgres psql -U edutech_user -d edutech < sql/consultas.sql

# Python
generate-data:
	python python/gerador_dados.py

validate-csv:
	python python/validador_csv.py

process-reports:
	python python/processador_relatorios.py

# Cleanup
clean:
	rm -rf data/*.csv
	docker-compose down -v