from django.db import models

from utils.model_mixin import CreateUpdateMixin
from project.utils.model_mixin import AccountMixin, CreatorMixin


class OrderStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    is_for_new_orders = models.BooleanField(default=True)


class OrderingType(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    тип оформления заказа:
    по телефону, на точке, в интернет магазине и т.д.
    """
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)


class OrderSource(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    откуда пришёл заказ:
    из яндекс.директ, из биглиона, из поисковой выдачи и т.д.
    """
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)


class PaymentType(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    наличные, безналичные и т.д.
    """
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
