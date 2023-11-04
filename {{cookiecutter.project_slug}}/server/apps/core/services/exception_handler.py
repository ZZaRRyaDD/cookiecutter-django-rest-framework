from rest_framework import response, status, views


def iterate_by_errors(errors: list, dict_errors: dict):
    """Func for iterate by errors"""
    for key, value in dict_errors.items():
        key_errors = {"field": key}
        if isinstance(value, (list, dict)):
            key_errors["message"] = check_errors_dict(value)
            errors.append(key_errors)
        else:
            errors.append(str(value))


def check_errors_dict(lst_errors: list | dict) -> str | list:
    """Function for recursive error traversal"""
    errors = []
    if isinstance(lst_errors, dict):
        iterate_by_errors(errors, lst_errors)
    elif isinstance(lst_errors, list):
        return lst_errors
    return errors


def get_errors(data: list | dict) -> list:
    """Entrypoint for get errors"""
    errors = []
    iterate_by_errors(errors, data)
    return errors


def custom_exception_handler(exc, context) -> response.Response | None:
    """Custom exception handler"""
    response = views.exception_handler(exc, context)
    if response:
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            response.data = {"detail": get_errors(response.data)}
        else:
            response.data = {"detail": response.data["detail"]}
    return response
