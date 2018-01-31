from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from .choices import CURRENCY_TYPE


class OrderingType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    тип (место) оформления:
    по телефону, на точке, в интернет магазине и т.д.
    """
    title = models.CharField(max_length=64)


class OrderingSource(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    источник оформления:
    из яндекс.директ, из биглиона, из поисковой выдачи и т.д.
    """
    title = models.CharField(max_length=64)


class PaymentType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    наличные, безналичные и т.д.
    """
    title = models.CharField(max_length=64)


class PriceType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    типы цен
    """
    PRICE_KIND = (
        (0, 'закупка'),
        (1, 'продажа'),
    )

    kind = models.PositiveSmallIntegerField(choices=PRICE_KIND, default=0)
    title = models.CharField(max_length=64)
    currency = models.PositiveSmallIntegerField(choices=CURRENCY_TYPE, default=0)
    notes = models.CharField(max_length=512)
