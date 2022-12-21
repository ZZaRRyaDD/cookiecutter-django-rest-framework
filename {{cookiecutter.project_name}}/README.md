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

{%- if cookiecutter.celery == "y" %}

### Celery

This app comes with Celery.

To run a celery worker:

``` bash
cd {{cookiecutter.project_slug}}
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

{%- endif %}
