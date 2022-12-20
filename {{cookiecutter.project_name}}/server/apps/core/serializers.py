from rest_framework import serializers


class BaseModelSerializer(serializers.ModelSerializer):
    """Serializer with common logic."""

    def __init__(self, *args, **kwargs):
        """Set current user."""
        super().__init__(*args, **kwargs)
        self._request = self.context.get("request")
        self._user = getattr(self._request, "user", None)
