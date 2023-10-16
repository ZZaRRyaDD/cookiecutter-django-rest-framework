from rest_framework import viewsets

from apps.core.services.pagination import PaginationObject


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet for other views."""

    pagination_class = PaginationObject
