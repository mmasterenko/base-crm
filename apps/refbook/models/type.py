from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from .choices import CURRENCY_TYPE


class OrderingMethod(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    КАК произошло оформление заказа, обращения:
    по телефону, на точке, в интернет магазине и т.д.
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'ordering_method'


class OrderingSource(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    ОТКУДА пришел заказ, обращение:
    из яндекс.директ, из биглиона, из поисковой выдачи и т.д.
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'ordering_source'


class PaymentType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    тип оплаты
    наличные, безналичные и т.д.
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'payment_type'


class PriceType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    типы цен
    """
    PRICE_KIND = (
        (0, 'закупка'),  # purchase
        (1, 'продажа'),  # selling
    )

    kind = models.PositiveSmallIntegerField(choices=PRICE_KIND, default=0)
    title = models.CharField(max_length=64)
    currency = models.PositiveSmallIntegerField(choices=CURRENCY_TYPE, default=0)
    notes = models.CharField(max_length=512)

    class Meta:
        db_table = 'price_type'


class IESource(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    статьи дохода / расхода
    """
    IE_KIND = (
        (0, 'статья расхода'),
        (1, 'статья дохода'),
    )
    ie_kind = models.PositiveSmallIntegerField(choices=IE_KIND)
    title = models.CharField(max_length=64)
    notes = models.CharField(max_length=512)

    class Meta:
        db_table = 'ie_source'
