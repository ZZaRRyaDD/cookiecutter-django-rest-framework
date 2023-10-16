from django.contrib.auth.models import User

from apps.core.serializers import BaseModelSerializer, serializers


class UserSerializer(BaseModelSerializer):
    """Serializer for User model."""

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
        )

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
