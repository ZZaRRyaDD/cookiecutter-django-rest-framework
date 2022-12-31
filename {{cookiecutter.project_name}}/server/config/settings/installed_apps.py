DJANGO_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
{%- if cookiecutter.websockets == 'n' %}
    "django.contrib.staticfiles",
{%- endif %}
    "django.contrib.admin",
    "django.forms",
]

THIRD_PARTY_APPS = [
{%- if cookiecutter.websockets != 'n' %}
    "daphne",
    "django.contrib.staticfiles",
{%- endif %}
    "rest_framework",
    "rest_framework.authtoken",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
{%- if cookiecutter.celery != 'n' %}
    "django_celery_beat",
{%- endif %}
    "corsheaders",
    "drf_spectacular",
    "django_filters",
    "django_extensions",
]

LOCAL_APPS = [
    "apps.core.apps.CoreConfig",
{%- if cookiecutter.websockets != 'n' %}
    "apps.chat.apps.ChatConfig",
{%- endif %}
    "apps.users.apps.UsersConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
