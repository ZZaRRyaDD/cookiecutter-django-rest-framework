# {{cookiecutter.project_name}}

{{ cookiecutter.description }}

[Built with Cookiecutter DjangoRestFrameowrk](https://github.com/PC-Nazarka/cookiecutter-django-rest-framework/)

## Basic Commands

For using install some libs:

```bash
pip install rich invoke
```

### Setting Up Your Users

-   To create a **superuser account**, use this command:

        $ inv django.createsuperuser
    By default have account with username admin, password admin, email admin@admin.com

#### Running tests with pytest

    $ inv tests.pytest

#### Running pinters - flake8, isort

    $ inv linters.all
