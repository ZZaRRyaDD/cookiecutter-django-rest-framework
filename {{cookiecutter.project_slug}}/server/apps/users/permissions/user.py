from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view) -> bool:
        return True

    def has_object_permission(self, request, view, obj) -> bool:
        if request.method == "PATCH":
            return request.user.id == obj.id
        return True
