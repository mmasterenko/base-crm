from django.db import models
from django.conf import settings
from django.utils import timezone

from apps.refbook.models import (Organisation, Shop, OrderingType, OrderStatus, OrderSource,
                                 PaymentType, CounterAgent)
from core.models import Country, Region, City
from utils.model_mixin import CreateUpdateMixin
from project.utils.model_mixin import AccountMixin


class Order(AccountMixin, CreateUpdateMixin, models.Model):
    """
    обратные связи:
    - товары
    - комментарии
    - связанные документы
    """
    PAYMENT_STATUS = (  # todo: закрепить в тестах
        (0, 'Не оплачен'),
        (1, 'Частично оплачен'),
        (2, 'Оплачен'),
    )

    # общее
    number = models.CharField(max_length=128, unique=True)
    date = models.DateTimeField(default=timezone.now)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)

    status = models.ForeignKey(OrderStatus, on_delete=models.PROTECT)
    source = models.ForeignKey(OrderSource, on_delete=models.PROTECT)
    ordering_type = models.ForeignKey(OrderingType, on_delete=models.PROTECT)  # тип оформления

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    # покупатель
    buyer = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)

    # доставка
    delivery_address_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    delivery_address_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    delivery_address_city = models.ForeignKey(City, on_delete=models.PROTECT)
    delivery_address_postcode = models.CharField(max_length=16)
    delivery_address_info = models.CharField(max_length=256)
    delivery_date = models.DateTimeField(default=timezone.now)

    # оплата
    payment_type = models.ForeignKey(PaymentType, on_delete=models.PROTECT)
    payment_status = models.PositiveSmallIntegerField(choices=PAYMENT_STATUS, default=0)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    paid_for = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class OrderLine(AccountMixin, CreateUpdateMixin, models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
