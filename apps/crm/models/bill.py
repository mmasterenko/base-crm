from django.db import models
from django.conf import settings
from django.utils import timezone

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from apps.refbook.models import Organisation, Shop, CounterAgent, Product


class Bill(AccountMixin, CreateUpdateMixin, CreatorMixin, ArchiveMixin, models.Model):
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
