from rest_framework import mixins, viewsets


class CreateRetrieveUpdateViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """CreateRetrieveUpdateViewSet for `create`, `read`, `list`, `update`."""
