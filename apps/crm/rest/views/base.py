from rest_framework.generics import ListCreateAPIView

from utils.rest_framework.generics import RetrieveUpdateDestroy
from apps.crm import models as crm_models
from apps.crm.rest import serializers as crm_serializers


class CustomerRequestListView(ListCreateAPIView):
    serializer_class = crm_serializers.CustomerRequestSerializer

    def get_queryset(self):
        return crm_models.CustomerRequest.objects.filter(is_archive=False)


class CustomerRequestDetailView(RetrieveUpdateDestroy):
    serializer_class = crm_serializers.CustomerRequestSerializer

    def get_queryset(self):
        return crm_models.CustomerRequest.objects.filter(is_archive=False)
