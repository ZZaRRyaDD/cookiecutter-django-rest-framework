from config.development import *  # noqa F401 F403
{% if cookiecutter.celery != 'n' %}
CELERY_TASK_ALWAYS_EAGER = True
{% endif %}