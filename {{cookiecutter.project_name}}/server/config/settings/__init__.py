{%- if cookiecutter.celery != 'n' -%}
from .celery import *
{% endif -%}
from .drf import *
from .email import *
from .installed_apps import *
from .settings import *
