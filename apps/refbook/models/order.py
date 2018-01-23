from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class OrderStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    статус заказа
    """
    title = models.CharField(max_length=64)
    is_for_new_orders = models.BooleanField(default=True)


class OrderingType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    тип оформления заказа:
    по телефону, на точке, в интернет магазине и т.д.
    """
    title = models.CharField(max_length=64)


class OrderSource(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    откуда пришёл заказ:
    из яндекс.директ, из биглиона, из поисковой выдачи и т.д.
    """
    title = models.CharField(max_length=64)


class PaymentType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    наличные, безналичные и т.д.
    """
    title = models.CharField(max_length=64)
