from django.db import models
from django.conf import settings
from django.utils import timezone

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from apps.refbook.models import CounterAgent, Shop, Organisation, CashNAccount, IncomeNExpenseType


class IncomeNExpense(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    приход / расход денег извне
    """
    IE_KIND = (
        (0, 'расход'),
        (1, 'доход'),
    )
    ie_kind = models.PositiveSmallIntegerField(choices=IE_KIND)
    is_made = models.BooleanField(default=True)  # проведен / учитывать
    source = models.ForeignKey(IncomeNExpenseType, on_delete=models.PROTECT)  # статья дохода/расхода
    cash_account = models.ForeignKey(CashNAccount, on_delete=models.PROTECT)
    datetime = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    vat = models.PositiveSmallIntegerField()
    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsible_for_ie',
                                    on_delete=models.PROTECT)

    class Meta:
        db_table = 'income_n_expense'


class MoneyFlow(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    перемещение денег внутри аккаунта
    """
    is_made = models.BooleanField(default=True)  # проведен / учитывать
    datetime = models.DateTimeField(default=timezone.now)
    cash_account_sender = models.ForeignKey(CashNAccount, related_name='as_sender_flows', on_delete=models.PROTECT)
    cash_account_receiver = models.ForeignKey(CashNAccount, related_name='as_receiver_flows', on_delete=models.PROTECT)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsible_for_money_flows',
                                    on_delete=models.PROTECT)

    class Meta:
        db_table = 'money_flow'
