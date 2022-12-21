# Cookiecutter DjangoRestFramework

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter DjangoRestFramework is a framework for jumpstarting
production-ready DjangoRestFramework projects quickly.

## Features

-   For Django 3.2.16
-   Works with Python 3.10
-   Optional basic ASGI setup for Websockets
-   Docker support using [docker-compose](https://github.com/docker/compose) for development and production
-   Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review

## Optional Integrations

*These features can be enabled during initial project setup.*

-   Configuration for [Celery](https://docs.celeryq.dev)
-   Configuration for Django-Channels with Daphne
-   Configuration nginx

## Usage

First, get Cookiecutter. Trust me, it's awesome:

    $ pip install "cookiecutter>=1.7.0"

Now run it against this repo:

    $ cookiecutter https://github.com/PC-Nazarka/cookiecutter-django-rest-framework

You'll be prompted for some values. Provide them, then a Django project will be created for you.

**Warning**: After this point, change 'ZZaRRyaDD' etc to your own information.

Answer the prompts with your own desired options. For example:

    Cloning into 'cookiecutter-django-rest-framework'...
    project_name [My project]:
    project_slug [my_project]:
    author_name [ZZaRRyaDD]:
    email [example@gmail.com]:
    description [My new django project]:
    timezone [UTC]: Asia/Krasnoyarsk
    Select websockets:
    1 - y
    2 - n
    Choose from 1, 2 [1]: 1
    Select nginx:
    1 - y
    2 - n
    Choose from 1, 2 [1]: 1
    Select celery:
    1 - y
    2 - n
    Choose from 1, 2 [1]: 1

Now take a look at your repo. Don't forget to carefully look at the generated README. Awesome, right?
