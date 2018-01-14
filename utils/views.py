from django.conf import settings
from django.views.static import serve
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ProtectedServe(APIView):
    schema = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, path, document_root=None, show_indexes=False):
        if document_root is None:
            document_root = settings.MEDIA_ROOT
        return serve(request, path, document_root, show_indexes)


class PatchProtectedServe(APIView):
    schema = None
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id, filename, document_root=None, show_indexes=False, **kwargs):
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return HttpResponseForbidden('403 Access Denied')
        else:
            if user != request.user:
                return HttpResponseForbidden('403 Access Denied')

        path = 'patches/user_{id}/{filename}'.format(id=request.user.id, filename=filename)

        if document_root is None:
            document_root = settings.MEDIA_ROOT
        return serve(request, path, document_root, show_indexes)
