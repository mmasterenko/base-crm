from django.db import models
from django.conf import settings

from core.models import Country, Region, City
from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from .choices import PROPERTY_TYPE


class CounterAgentGroup(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    группа/категория контрагентов (один контрагент может быть в нескольких категориях)
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'counter_agent_group'


class CounterAgentSegment(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    группа/категория контрагентов (один контрагент может быть в нескольких категориях)
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'counter_agent_segment'


class CounterAgent(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    контрагент - может быть ИП, ООО, физ.лицо и т.д.
    """
    AGENT_TYPE = (
        (0, 'физическое лицо'),
        (1, 'юридическое лицо'),
    )

    SEX = (
        (0, 'неизвестно'),
        (1, 'мужчина'),
        (2, 'женщина'),
    )

    # контрагент
    agent_type = models.PositiveSmallIntegerField(choices=AGENT_TYPE)
    title = models.CharField(max_length=256, unique=True)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    segments = models.ManyToManyField(CounterAgentSegment, related_name='counter_agents')
    # данные по контрагенту
    contact_name = models.CharField(max_length=128)
    sex = models.PositiveSmallIntegerField(choices=SEX, default=0)
    birth_date = models.DateField(blank=True, null=True)
    groups = models.ManyToManyField(CounterAgentGroup, related_name='counter_agents')
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsible_for_counter_agents',
                                    on_delete=models.PROTECT)
    # тип собственности и официальное название
    property_type = models.PositiveSmallIntegerField(choices=PROPERTY_TYPE)
    formal_title = models.CharField(max_length=256)
    # реквизиты
    inn = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ИНН
    kpp = models.CharField(max_length=64, blank=True, null=True, unique=True)   # КПП
    ogrn = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ОГРН
    okpo = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ОКПО
    # банковские реквизиты
    bik = models.CharField(max_length=64, blank=True, null=True, unique=True)  # БИК
    bank_title = models.CharField(max_length=256, blank=True, null=True)  # название банка
    korr_account = models.CharField(max_length=64, blank=True, null=True)  # корр.счёт
    account_number = models.CharField(max_length=64, blank=True, null=True)  # номер счёта
    account_title = models.CharField(max_length=256, blank=True, null=True)  # наименование счёта
    # юридический адрес
    legal_address_country = models.ForeignKey(Country, related_name='counter_agents_here', on_delete=models.PROTECT)
    legal_address_region = models.ForeignKey(Region, related_name='counter_agents_here', on_delete=models.PROTECT)
    legal_address_city = models.ForeignKey(City, related_name='counter_agents_here', on_delete=models.PROTECT)
    legal_address_postcode = models.CharField(max_length=16)
    legal_address_info = models.CharField(max_length=256)
    # фактический адрес
    fact_address_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    fact_address_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    fact_address_city = models.ForeignKey(City, on_delete=models.PROTECT)
    fact_address_postcode = models.CharField(max_length=16)
    fact_address_info = models.CharField(max_length=256)

    class Meta:
        db_table = 'counter_agent'
