from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.core.views import RetrieveUpdateViewSet

from .serializers import UserSerializer


class UserViewSet(RetrieveUpdateViewSet):
    serializer_class = UserSerializer
    lookup_field = "username"

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

    @action(methods=("GET",), detail=False)
    def me(self, request):
        return Response(
            data=(
                UserSerializer(request.user, context={"request": request}).data
            ),
            status=status.HTTP_200_OK,
        )
