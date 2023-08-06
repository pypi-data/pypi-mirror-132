.PHONY: pip install run gunicorn db-migrate db-upgrade db db-init black

pip:
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install -e .
	PIP_CONFIG_FILE=$(PWD)/pip.conf \
	pip install pytest pytest-cov black importanize pre-commit

install: pip
	pre-commit install

run:
	SETTINGS=$(PWD)/configs/local.ini FLASK_APP=project_name \
	FLASK_DEBUG=1 \
	flask run

gunicorn:
	SETTINGS=$(PWD)/configs/local.ini \
	$(PWD)/bin/project_name-cli gunicorn

db-migrate:
	SETTINGS=$(PWD)/configs/local.ini \
	alembic revision --autogenerate

db-upgrade:
	SETTINGS=$(PWD)/configs/local.ini \
	alembic upgrade head

db-downgrade:
	SETTINGS=$(PWD)/configs/local.ini \
	alembic downgrade -1

db:
	SETTINGS=$(PWD)/configs/local.ini \
	alembic upgrade head

db-init:
	SETTINGS=$(PWD)/configs/local.ini \
	alembic init alembic

black:
	python -m black project_name
