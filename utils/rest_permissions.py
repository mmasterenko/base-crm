from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAuthenticatedOrOptions(BasePermission):
    """
    The request is authenticated as a user, or is a OPTIONS request.
    """

    def has_permission(self, request, view):
        return (
            request.method == 'OPTIONS' or
            request.user and request.user.is_authenticated
        )


class IsAdminUserOrOptions(BasePermission):

    def has_permission(self, request, view):
        return (
            request.method == 'OPTIONS' or
            request.user and request.user.is_staff
        )


class IsStaffOrReadOnly(BasePermission):
    """
    Allows write access only to admin users and read access for all.
    For use with IsAuthenticated permission.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and (request.user.is_staff or request.user.is_superuser)
        )


class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser
