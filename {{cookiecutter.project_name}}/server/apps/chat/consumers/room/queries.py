from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from django.db.models import QuerySet


class UserQueries:

    @staticmethod
    @database_sync_to_async
    def get_users_list() -> QuerySet:
        return User.objects.all()
