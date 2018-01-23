from django.db import models

from utils.model_mixin import CreateUpdateMixin
from project.utils.model_mixin import AccountMixin, CreatorMixin

# todo: подумать над тем, чтобы заменить is_active на is_archive и сделать это через mixin


class OrderStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    статус заказа
    """
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


class Unit(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    единица измерения (эта таблица должна быть предварительно заполнена)
    """
    title = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
