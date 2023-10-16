from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.viewsets import CreateRetrieveUpdateViewSet
from apps.users.permissions import UserPermission
from apps.users.serializers import UserSerializer


class UserViewSet(CreateRetrieveUpdateViewSet):
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(methods=("GET",), detail=False)
    def me(self, request):
        if not request.user.is_authenticated:
            return Response(
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response(
            data=UserSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )
