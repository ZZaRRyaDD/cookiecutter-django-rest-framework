from channels.db import database_sync_to_async
from django.db.models import QuerySet

from apps.users.serializers import UserSerializer


class UserService:

    @staticmethod
    @database_sync_to_async
    def get_users_list(users: QuerySet) -> list:
        return UserSerializer(users, many=True).data
