from django.db import models

from utils.model_mixin import CreateUpdateMixin
from project.utils.model_mixin import AccountMixin, CreatorMixin
from core.models import Country
from . import Unit


class Organisation(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    pass


class Shop(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    pass


class CounterAgent(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    контрагент - может быть ИП, ООО, физ.лицо и т.д.
    """
    pass


class ProductGroup(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    title = models.CharField(max_length=64)


class Product(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    товар
    """
    PRODUCT_TYPE = (
        (0, 'Товар'),
        (1, 'Услуга'),
        (2, 'Набор'),
    )

    is_active = models.BooleanField(default=True)
    title = models.CharField(max_length=256)

    article = models.CharField(max_length=64)
    bar_code = models.CharField(max_length=32)

    groups = models.ManyToManyField(ProductGroup)
    unit = models.ForeignKey(Unit, blank=True, null=True, on_delete=models.SET_NULL)
    product_type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPE)
    selling_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    vat = models.PositiveSmallIntegerField(default=0)  # НДС (value-added tax)
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.SET_NULL)
