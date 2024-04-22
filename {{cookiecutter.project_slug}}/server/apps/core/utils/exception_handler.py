from rest_framework import (
    exceptions,
    response,
    views,
)


def get_errors(details):
    detail = []
    if isinstance(details, dict):
        for key, value in details.items():
            detail.append({"field": key, "message": value})
    else:
        detail.append({"field": "non_field_errors", "message": details})
    return detail


def custom_exception_handler(exc, context) -> response.Response | None:
    """Custom exception handler"""
    if isinstance(exc, exceptions.ValidationError):
        exc.detail = get_errors(exc.detail)
    response = views.exception_handler(exc, context)
    return response
