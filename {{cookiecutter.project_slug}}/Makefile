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

docker-up-build:  ##@Application Run and build application server
	docker-compose up --build --remove-orphans

docker-up-buildd:  ##@Application Run and build application server in daemon
	docker-compose up -d --build --remove-orphans

docker-up:  ##@Application Run application server
	docker-compose up

docker-upd:  ##@Application Run application server in daemon
	docker-compose up -d

docker-up-build-prod:  ##@Application Run application server in prod
	docker-compose -f docker-compose.prod.yml up --build --remove-orphans

docker-up-buildd-prod:  ##@Application Run application server in prod in daemon
	docker-compose -f docker-compose.prod.yml up -d --build --remove-orphans

docker-down:  ##@Application Stop application in docker
	docker-compose down --remove-orphans

docker-downv:  ##@Application Stop application in docker and remove volumes
	docker-compose down -v --remove-orphans

docker-down-prod:  ##@Application Stop application in docker in prod
	docker-compose -f docker-compose.prod.yml down --remove-orphans

docker-downv-prod:  ##@Application Stop application in docker and remove volumes in prod
	docker-compose -f docker-compose.prod.yml down -v --remove-orphans

docker-django-run:  ##@Application Run django container with command
	docker-compose run --rm django $(args)

docker-django-run-prod:  ##@Application Run django container with command in prod
	docker-compose -f docker-compose.prod.yml run --rm django $(args)

fill_sample_data:  ##@Application Run script for create sample data in db
	make docker-django-run "python manage.py runscript fill_sample_data"

migrate:  ##@Application Apply migrations
	make docker-django-run "python manage.py migrate"

makemigrations:  ##@Application Create migrations
	make docker-django-run "python manage.py makemigrations"

createsuperuser:  ##@Application Create superuser
	make docker-django-run "python manage.py createsuperuser"

migrate-prod:  ##@Application Apply migrations in prod
	make docker-django-run-prod "python manage.py migrate"

shell:  ##@Application Run django shell
	make docker-django-run "python manage.py shell"

open-db:  ##@Database Open database inside docker-image
	docker exec -it postgres psql -d $(POSTGRES_DB) -U $(POSTGRES_USER) -p $(POSTGRES_PORT)

tests:  ##@Testing Test application with pytest
	make docker-django-run pytest

tests-cov:  ##@Testing Test application with pytest and create coverage report
	make docker-django-run pytest "--verbosity=2 --showlocals --log-level=DEBUG --full-trace"

linters:  ##@Linters Run linters
	make docker-django-run "isort . --settings-file=./setup.cfg"
	make docker-django-run "flake8 . --config=./setup.cfg"

docker-clean:  ##@Application Remove all docker objects
	docker system prune -f

docker-clean-all:  ##@Application Remove all unused docker objects
	docker system prune --all -f

docker-clean-allv:  ##@Application Remove all docker objects with volumes
	docker system prune --all --volumes -f

docker-stop:  ##@Application Stop all docker containers
	@docker container rm -f $$(docker ps -aq) || true

%::
	echo $(MESSAGE)
