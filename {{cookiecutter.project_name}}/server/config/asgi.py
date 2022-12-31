import os
{% if cookiecutter.websockets != 'n' %}
import django
from channels.routing import get_default_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
application = get_default_application()
{%- else %}
from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

application = get_asgi_application()
{%- endif %}
