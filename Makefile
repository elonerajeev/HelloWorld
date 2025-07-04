.PHONY: help install test lint format clean docker-build docker-run docker-compose-up docker-compose-down

help:
	@echo "Available commands:"
	@echo "  install          - Install dependencies"
	@echo "  test             - Run tests"
	@echo "  lint             - Run linting"
	@echo "  format           - Format code"
	@echo "  clean            - Clean up files"
	@echo "  docker-build     - Build Docker image"
	@echo "  docker-run       - Run Docker container"
	@echo "  docker-compose-up - Start with docker-compose"
	@echo "  docker-compose-down - Stop docker-compose"

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v --cov=app --cov-report=html

lint:
	flake8 .
	black --check .

format:
	black .

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .coverage

docker-build:
	docker build -t helloworld-app .

docker-run:
	docker run -p 5000:5000 helloworld-app

docker-compose-up:
	docker-compose up -d

docker-compose-down:
	docker-compose down
