from config.settings import *  # noqa F401 F403

{% if cookiecutter.celery == 'y' %}
CELERY_TASK_ALWAYS_EAGER = True
{% endif %}