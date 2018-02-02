from django.db import models
from django.conf import settings
from django.utils import timezone

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from core.models import Country, Region, City
from apps.refbook.models import (Organisation, Shop, OrderingMethod, OrderStatus, OrderingSource,
                                 PaymentType, CounterAgent, Product)


class Order(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
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
    ordering_source = models.ForeignKey(OrderingSource, on_delete=models.PROTECT)  # источник оформления
    ordering_method = models.ForeignKey(OrderingMethod, on_delete=models.PROTECT)  # тип оформления

    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='responsible_for_orders',
                                    on_delete=models.SET_NULL)

    # покупатель
    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)

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


class OrderLine(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    строка товар - в таблице товары (в Заказе)
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    count = models.PositiveIntegerField(default=0)  # кол-во
    discount = models.PositiveSmallIntegerField(default=0)  # скидка на данную позицию
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
