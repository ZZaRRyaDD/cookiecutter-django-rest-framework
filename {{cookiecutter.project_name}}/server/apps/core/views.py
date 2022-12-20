from rest_framework import mixins, viewsets

from .services.pagination import PaginationObject


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet for other views."""

    pagination_class = PaginationObject


class RetrieveUpdateViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    """RetrieveUpdateViewSet for `read`, `list`, `update`."""
