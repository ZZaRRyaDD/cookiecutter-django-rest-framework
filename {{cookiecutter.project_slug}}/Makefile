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

env:  ##@Application Create env file
	cp .env.example .env

docker-up-build:  ##@Application Run and build application server
	docker-compose up --build --remove-orphans

docker-up-buildd:  ##@Application Run and build application server in daemon
	docker-compose up -d --build --remove-orphans

docker-up:  ##@Application Run application server
	docker-compose up

docker-upd:  ##@Application Run application server in daemon
	docker-compose up -d

docker-down:  ##@Application Stop application in docker
	docker-compose down --remove-orphans

docker-downv:  ##@Application Stop application in docker and remove volumes
	docker-compose down -v --remove-orphans

docker-django-run:  ##@Application Run django container with command
	docker-compose run --rm django $(args)

docker-django-prod-run:  ##@Application Run django production container with command
	docker-compose -f docker-compose.prod.yml run --rm django $(args)

fill_sample_data:  ##@Application Run script for create sample data in db
	make docker-django-run "make fill_sample_data"

migrate:  ##@Application Apply migrations
	make docker-django-run "make migrate"

makemigrations:  ##@Application Create migrations
	make docker-django-run "make makemigrations"

createsuperuser:  ##@Application Create superuser
	make docker-django-run "make createsuperuser"

shell:  ##@Application Run django shell
	make docker-django-run "make shell"

open-db:  ##@Database Open database inside docker-image
	docker exec -it postgres psql -d $(POSTGRES_DB) -U $(POSTGRES_USER) -p $(POSTGRES_PORT)

tests:  ##@Testing Test application with pytest
	make docker-django-run "make tests"

tests-cov:  ##@Testing Test application with pytest and create coverage report
	make docker-django-run "make tests-cov"

linters:  ##@Linters Run linters
	make docker-django-run "make linters"

docker-clean:  ##@Docker Remove all unused docker objects
	docker system prune --all -f

docker-cleanv:  ##@Docker Remove all docker objects with volumes
	docker system prune --all --volumes -f

docker-pull-prod:  ##@Docker Pulling containers
	docker-compose -f docker-compose.prod.yml pull

docker-stop:  ##@Docker Stop all docker containers
	@docker rm -f $$(docker ps -aq) || true

%::
	echo $(MESSAGE)
