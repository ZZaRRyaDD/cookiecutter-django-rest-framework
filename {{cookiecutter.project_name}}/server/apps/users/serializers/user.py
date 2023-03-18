from django.contrib.auth.models import User

from apps.core.serializers import BaseModelSerializer


class UserSerializer(BaseModelSerializer):
    """Serializer for User model."""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
        )
        extra_kwargs = {
            "password": {"write_only": True}
        }
