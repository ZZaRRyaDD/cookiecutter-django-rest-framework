from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.viewsets import RetrieveUpdateViewSet
from apps.users.serializers import UserSerializer


class UserViewSet(RetrieveUpdateViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    @action(methods=("GET",), detail=False)
    def me(self, request):
        return Response(
            data=UserSerializer(request.user).data,
            status=status.HTTP_200_OK,
        )
