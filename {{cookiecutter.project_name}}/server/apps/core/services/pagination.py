from rest_framework import pagination, response


class PaginationObject(pagination.PageNumberPagination):
    """Class for paginate object."""

    page_size_query_param = 'page_size'
    page_size = 9

    def get_paginated_response(self, data):
        """Overriden for get links on previous and next pages."""
        return response.Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            },
        )
