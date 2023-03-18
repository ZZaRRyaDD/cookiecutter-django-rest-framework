from rest_framework import mixins, viewsets


class RetrieveUpdateViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """RetrieveUpdateViewSet for `read`, `list`, `update`."""
