from rest_framework.authentication import SessionAuthentication
from django.conf import settings


class SessionAuthenticationWithCSRFFix(SessionAuthentication):
    """
    It is extends rest_framework's SessionAuthentication class for uses with CSRF_CHECK setting
    """
    def enforce_csrf(self, request):
        if settings.CSRF_CHECK:
            return super().enforce_csrf(request)
        else:
            pass
