from rest_framework import viewsets

from apps.core.utils import PaginationObject


class BaseViewSet(viewsets.ModelViewSet):
    """Base ViewSet for other views."""

    pagination_class = PaginationObject
