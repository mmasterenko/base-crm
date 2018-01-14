from collections import OrderedDict

from django.core import mail
from django.core.mail import get_connection
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import serializers
from constance import config


class SettingsSerializer(serializers.Serializer):

    smtp_username = serializers.CharField(required=False)
    smtp_password = serializers.CharField(required=False)
    smtp_host = serializers.CharField(required=False)
    smtp_port = serializers.IntegerField(required=False)
    use_tls = serializers.BooleanField(required=False)


class AdminSettingsView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

    # note !
    # having added new keys in this list, make sure add them to SettingsSerializer
    constance_keys = [
        'SMTP_USERNAME',
        'SMTP_PASSWORD',
        'SMTP_HOST',
        'SMTP_PORT',
        'USE_TLS',
    ]

    def get(self, request):
        response = OrderedDict()
        for key in self.constance_keys:
            response[key.lower()] = getattr(config, key)
        return Response(response)

    def patch(self, request):
        serializer = SettingsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        response = OrderedDict()
        for key in self.constance_keys:
            if key.lower() in serializer.validated_data:
                value = serializer.validated_data[key.lower()]
                setattr(config, key, value)
            response[key.lower()] = getattr(config, key)
        return Response(response)


class SettingsView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    constance_keys = [
        'YK_SHOP_ID',
        'YK_SC_ID',
        'YK_URL',
    ]

    def get(self, request):
        response = OrderedDict()
        for key in self.constance_keys:
            response[key.lower()] = getattr(config, key)
        return Response(response)


def except_view(request):
    raise Exception


def test_mail_view(request):
    mail.mail_admins(subject='test subject',
                     message='test message',
                     connection=get_connection(fail_silently=False),
                     fail_silently=False)
    return HttpResponse('OK')
