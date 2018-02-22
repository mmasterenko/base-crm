from django.db import models
from django.conf import settings
from django.utils import timezone

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from apps.refbook.models import CounterAgent, Shop, Organisation, CashNAccount, IncomeNExpenseType


class IncomeNExpense(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    Доходы и Расходы - помещено в одну сущность, потому что они очень похожи.
    Эта сущность отражает денежное взаимодействие аккаунта с внешним миром.
    """
    IE_KIND = (
        (0, 'расход'),
        (1, 'доход'),
    )
    ie_kind = models.PositiveSmallIntegerField(verbose_name='вид',
                                               choices=IE_KIND)
    is_made = models.BooleanField(verbose_name='проведен',
                                  default=True)
    source = models.ForeignKey(IncomeNExpenseType,
                               verbose_name='статья',
                               help_text='статья дохода/расхода',
                               on_delete=models.PROTECT)
    cash_account = models.ForeignKey(CashNAccount,
                                     verbose_name='касса/расчетный счет',
                                     on_delete=models.PROTECT)
    datetime = models.DateTimeField(verbose_name='время операции',
                                    default=timezone.now)
    amount = models.DecimalField(verbose_name='сумма',
                                 help_text='сумма перевода (в рублях)',
                                 max_digits=10,
                                 decimal_places=2)
    vat = models.PositiveSmallIntegerField(verbose_name='НДС, %')
    counter_agent = models.ForeignKey(CounterAgent,
                                      verbose_name='контрагент',
                                      on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation,
                                     verbose_name='организация',
                                     on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name='ответственный',
                                    related_name='responsible_for_ie',
                                    on_delete=models.PROTECT)

    class Meta:
        db_table = 'income_n_expense'
        verbose_name = 'IncomeNExpense (Доходы/Расходы)'


class MoneyFlow(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    Перемещения денежных средств - эта сущность отражает
    денежные потоки внутри аккаунта.
    """
    is_made = models.BooleanField(verbose_name='проведен',
                                  help_text='если этот флаг не установлен, тогда это перемещение нигде не учитывать',
                                  default=True)
    datetime = models.DateTimeField(verbose_name='время операции',
                                    default=timezone.now)
    cash_account_sender = models.ForeignKey(CashNAccount,
                                            verbose_name='отправитель',
                                            related_name='as_sender_flows',
                                            on_delete=models.PROTECT)
    cash_account_receiver = models.ForeignKey(CashNAccount,
                                              verbose_name='получатель',
                                              related_name='as_receiver_flows',
                                              on_delete=models.PROTECT)
    amount = models.DecimalField(verbose_name='сумма',
                                 default=0,
                                 max_digits=10,
                                 decimal_places=2)
    organisation = models.ForeignKey(Organisation,
                                     verbose_name='организация',
                                     on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL,
                                    verbose_name='ответственный',
                                    related_name='responsible_for_money_flows',
                                    on_delete=models.PROTECT)

    class Meta:
        db_table = 'money_flow'
        verbose_name = 'MoneyFlow (Перемещение ДС)'
