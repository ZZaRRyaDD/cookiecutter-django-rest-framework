# Cookiecutter DjangoRestFramework

Powered by [Cookiecutter](https://github.com/cookiecutter/cookiecutter), Cookiecutter DjangoRestFramework is a framework for jumpstarting
production-ready DjangoRestFramework projects quickly.

## Features

-   For Django 4.2.1
-   Works with Python 3.10
-   Docker support using docker-compose for development and production

## Optional Integrations

*These features can be enabled during initial project setup.*

-   Configuration for Celery, Flower
-   Configuration for Django-Channels with Daphne
-   Auth deploy with GitHub Actions

## Usage

Get Cookiecutter:

```bash
pip install "cookiecutter>=1.7.0"
```

Now run it for generate project with this template:

```bash
cookiecutter https://github.com/PC-Nazarka/cookiecutter-django-rest-framework
```

You'll be prompted for some values. Provide them, then a Django project will be created for you.

Answer the prompts with your own desired options. For example:

    Cloning into 'cookiecutter-django-rest-framework'...
    project_name [My project]:
    project_slug [my_project]:
    author_name [ZZaRRyaDD]:
    email [example@gmail.com]:
    description [My new django project]:
    timezone [UTC]: Asia/Krasnoyarsk
    websockets [n]:
    celery [n]:
    autodeploy [n]:


Now take a look at your repo.
