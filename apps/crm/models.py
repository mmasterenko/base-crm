from django.db import models
from django.conf import settings
from django.utils import timezone

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from core.models import Country, Region, City
from apps.refbook.models import (Organisation, Shop, OrderingType, OrderStatus, OrderingSource,
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
    ordering_type = models.ForeignKey(OrderingType, on_delete=models.PROTECT)  # тип оформления

    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

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


class TaskStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    title = models.CharField(max_length=64)


class Task(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    задачи
    """
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    text = models.TextField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)
    base_on_ref = None  # (документ основание) ссылка на другую сущность: Заказы, Обращение и т.д.


class CustomerRequestStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    статус обращения
    """
    title = models.CharField(max_length=64)


class CustomerRequest(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    обращения пользователей
    """
    datetime = models.DateTimeField(default=timezone.now)

    status = models.ForeignKey(CustomerRequestStatus, on_delete=models.PROTECT)  # статус
    ordering_source = models.ForeignKey(OrderingSource, on_delete=models.PROTECT)  # источник оформления
    ordering_type = models.ForeignKey(OrderingType, on_delete=models.PROTECT)  # тип оформления

    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    text = models.TextField()  # цель обращения

    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)


class VoiceCall(AccountMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    звонки
    """
    datetime = models.DateTimeField(default=timezone.now)
    ordering_source = models.ForeignKey(OrderingSource, on_delete=models.PROTECT)  # источник оформления
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)


class Bill(AccountMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    розничные чеки
    """
    datetime = models.DateTimeField(default=timezone.now)
    # данные по чеку
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    # покупатель
    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)
    # оплата
    payment_type = None  # todo: ???
    paid_for = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class BillLine(AccountMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    строка в таблице Чеки покупателей
    """
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL)
    count = models.PositiveIntegerField(default=0)  # кол-во
    discount = models.PositiveSmallIntegerField(default=0)  # скидка на данную позицию
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
