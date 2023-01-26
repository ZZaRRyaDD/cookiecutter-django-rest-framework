# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

[Built with Cookiecutter DjangoRestFramework](https://github.com/PC-Nazarka/cookiecutter-django-rest-framework/)

## Basic Commands

For using install some libs:

```bash
pip install rich invoke
```

### Setting Up Your Users
To create a **superuser account**, use this command:

```bash
inv django.createsuperuser
```

By default have account with username admin, password admin, email admin@admin.com

#### Running tests with pytest

```bash
inv tests.pytest
```

#### Running linters - flake8, isort

```bash
inv linters.all
```
