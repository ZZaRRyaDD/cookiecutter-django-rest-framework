from django.contrib.auth.models import User

from .schedules import app


@app.task
def user_count() -> None:
    print(f"Count users in project: {User.objects.count()}")
