from django.contrib.auth.models import User

from config.celery import app


@app.task
def user_count() -> None:
    print(User.objects.count())
