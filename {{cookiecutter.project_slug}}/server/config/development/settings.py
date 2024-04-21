import os
from pathlib import Path

import dj_database_url

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent

# GENERAL
# ------------------------------------------------------------------------------
APP_LABEL = "{{cookiecutter.project_name}}"
DEBUG = os.environ.get("DJANGO_DEBUG", "false") == "true"
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "vqBuvYRdQrAHdKY3bMyvV8wvuy6QaczedCQrmb58YVR3bjY8avnxFXNumWuqdb6s",
)

TIME_ZONE = "{{cookiecutter.timezone}}"
LANGUAGE_CODE = "ru"
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"
{%- if cookiecutter.websockets != 'n' %}
ASGI_APPLICATION = 'config.routing.application'
{%- endif %}

ALLOWED_HOSTS = ["*"]

# DATABASES
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASES = {'default': dj_database_url.config(conn_max_age=60)}

REDIS_URL = os.getenv('REDIS_URL')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
    }
}
{% if cookiecutter.websockets != 'n' %}
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],
        },
    },
}
{% endif %}
# AUTHENTICATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# PASSWORDS
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.common.BrokenLinkEmailsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(ROOT_DIR / "staticfiles")
STATIC_URL = "/static/"
STATICFILES_DIRS = [str(ROOT_DIR / "static")]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
MEDIA_ROOT = str(ROOT_DIR / "media")
MEDIA_URL = "/media/"

# TEMPLATES
# ------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(ROOT_DIR / "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ADMIN
# ------------------------------------------------------------------------------
ADMIN_URL = os.getenv("DJANGO_ADMIN_URL", "admin/")

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s "
            "%(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console", "mail_admins"],
            "propagate": True,
        },
    },
}

# django-debug-toolbar
# ------------------------------------------------------------------------------
if DEBUG:
    import socket

    from .installed_apps import INSTALLED_APPS

    def show_toolbar(request):
        from django.conf import settings
        return settings.DEBUG

    DEBUG_TOOLBAR_CONFIG = {
        "SHOW_TEMPLATE_CONTEXT": show_toolbar,
    }
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INSTALLED_APPS += ['debug_toolbar']
    INTERNAL_IPS = (
        "0.0.0.0",
        "127.0.0.1",
    )
    ip = socket.gethostbyname(socket.gethostname())
    INTERNAL_IPS += (ip[:-1] + "1",)
