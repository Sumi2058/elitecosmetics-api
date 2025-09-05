migration:
	python3 manage.py makemigrations sellers

migrate:
	python3 manage.py migrate

run:
	python3 manage.py runserver

db:
	docker run --name postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=elitecosmetics -p 5432:5432 -d postgres:15

project:
	django-admin startproject my_tennis_club

app:
	python3.12 manage.py startapp auth


build:
	docker build -t sumi2058/elitecosmetics:v1.0.0 .

push:
	docker push sumi2058/elitecosmetics:v1.0.0

docker-run:
	docker run -p 8000:8000 --name pythonapp -d sumi2058/elitecosmetics:v1.0.0

docker-log:
	docker logs containername

docker-shell:
	docker exec -it pythonapp bash

dep:
	pip install -r requirements.txt

venv:
	python3 -m venv venv
