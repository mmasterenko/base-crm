from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from core.models import Country


class Unit(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    единица измерения (эта таблица должна быть предварительно заполнена)
    """
    title = models.CharField(max_length=64)
    short = models.CharField(max_length=16)
    by_default = models.BooleanField(default=True)

    class Meta:
        db_table = 'unit'


class ProductGroup(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    группа/категория товаров (один товар может быть в нескольких категориях)
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'product_group'


class Product(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    товар

    ещё добавить:
    товары в наборе
    характеристики
    модификации
    """
    PRODUCT_TYPE = (
        (0, 'Товар'),
        (1, 'Услуга'),
        (2, 'Набор'),
    )

    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    article = models.CharField(max_length=64)
    bar_code = models.CharField(max_length=32)

    groups = models.ManyToManyField(ProductGroup, related_name='products')
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.SET_NULL)
    product_type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPE)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    vat = models.PositiveSmallIntegerField(default=0)  # НДС (value-added tax)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'product'
