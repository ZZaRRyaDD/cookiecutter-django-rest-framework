ifeq ($(shell test -e '.env' && echo -n yes),yes)
	include .env
endif

args := $(wordlist 2, 100, $(MAKECMDGOALS))
ifndef args
MESSAGE = "No such command (or you pass two or many targets to ). List of possible commands: make help"
else
MESSAGE = "Done"
endif

HELP_FUN = \
	%help; while(<>){push@{$$help{$$2//'options'}},[$$1,$$3] \
	if/^([\w-_]+)\s*:.*\#\#(?:@(\w+))?\s(.*)$$/}; \
    print"$$_:\n", map"  $$_->[0]".(" "x(20-length($$_->[0])))."$$_->[1]\n",\
    @{$$help{$$_}},"\n" for keys %help; \


# Commands
help: ##@Help Show this help
	@echo -e "Usage: make [target] ...\n"
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

fill_sample_data:  ##@ApplicationDev Run script for create sample data in db
	python manage.py runscript fill_sample_data

migrate:  ##@ApplicationDev Apply migrations
	python manage.py migrate

makemigrations:  ##@ApplicationDev Create migrations
	python manage.py makemigrations

createsuperuser:  ##@ApplicationDev Create superuser
	python manage.py createsuperuser

shell:  ##@ApplicationDev Run django shell
	python manage.py shell

tests:  ##@Testing Test application with pytest
	pytest -n 3 --disable-pytest-warnings --verbosity=2 --showlocals --log-level=INFO --full-trace

tests-cov:  ##@Testing Test application with pytest and create coverage report
	coverage run -m pytest --cov-config=setup.cfg
	coverage html

linters:  ##@Linters Run linters
	isort . --settings-file=./setup.cfg
	flake8 . --config=./setup.cfg

run-django-dev:  ##@ApplicationDev Run django
	python manage.py runserver 0.0.0.0:8000

run-django-prod:  ##@ApplicationProd Run django in production
	gunicorn config.wsgi -c ./config/gunicorn.py

run-daphne-prod:  ##@ApplicationProd Run daphne in production
	daphne -b 0.0.0.0 -p $(DAPHNE_PORT) config.asgi:application --access-log ./logs/daphne.log -v 3

%::
	echo $(MESSAGE)
