from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.crm import models as crm_models
from apps.refbook import models as rb_models

User = get_user_model()


class CustomerRequestSerializer(serializers.ModelSerializer):
    status_id = serializers.PrimaryKeyRelatedField(
        source='status',
        queryset=rb_models.CustomerRequestStatus.objects.filter(is_archive=True)
    )
    ordering_source_id = serializers.PrimaryKeyRelatedField(
        source='ordering_source',
        queryset=rb_models.OrderingSource.objects.filter(is_archive=True)
    )
    ordering_method_id = serializers.PrimaryKeyRelatedField(
        source='ordering_method',
        queryset=rb_models.OrderingMethod.objects.filter(is_archive=True)
    )
    shop_id = serializers.PrimaryKeyRelatedField(
        source='shop',
        queryset=rb_models.Shop.objects.filter(is_archive=True)
    )
    responsible_id = serializers.PrimaryKeyRelatedField(
        source='responsible',
        queryset=User.objects.filter(is_archive=True)
    )
    counter_agent_id = serializers.PrimaryKeyRelatedField(
        source='counter_agent',
        queryset=rb_models.CounterAgent.objects.filter(is_archive=True)
    )
    organisation_id = serializers.PrimaryKeyRelatedField(
        source='organisation',
        queryset=rb_models.Organisation.objects.filter(is_archive=True)
    )

    class Meta:
        model = crm_models.CustomerRequest
        fields = [
            'datetime',
            'text',
            'status_id',
            'ordering_source_id',
            'ordering_method_id',
            'shop_id',
            'responsible_id',
            'counter_agent_id',
            'organisation_id',
        ]
