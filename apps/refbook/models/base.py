from django.db import models
from django.conf import settings

from core.models import Country, Region, City
from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class PriceType(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    типы цен
    """
    KIND = (
        (0, 'закупка'),
        (1, 'продажа'),
    )

    CURRENCY_TYPE = (
        (0, 'RUB'),
    )

    kind = models.PositiveSmallIntegerField(choices=KIND, default=0)
    title = models.CharField(max_length=64)
    currency = models.PositiveSmallIntegerField(choices=CURRENCY_TYPE, default=0)
    note = models.CharField(max_length=512)


class Organisation(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    pass


class Shop(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    pass


class CounterAgentGroup(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    группа/категория контрагентов (один контрагент может быть в нескольких категориях)
    """
    title = models.CharField(max_length=64)


class CounterAgentSegment(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    группа/категория контрагентов (один контрагент может быть в нескольких категориях)
    """
    title = models.CharField(max_length=64)


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

    PROPERTY_TYPE = (
        (0, 'ИП'),
        (1, 'ООО'),
        (2, 'ОАО'),
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
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    # реквизиты
    property_type = models.PositiveSmallIntegerField(choices=PROPERTY_TYPE)
    formal_title = models.CharField(max_length=256)

    inn = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ИНН
    kpp = models.CharField(max_length=64, blank=True, null=True, unique=True)   # КПП
    ogrn = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ОГРН
    okpo = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ОКПО

    bik = models.CharField(max_length=64, blank=True, null=True, unique=True)  # БИК
    bank_title = models.CharField(max_length=256, blank=True, null=True)  # название банка
    korr_account = models.CharField(max_length=64, blank=True, null=True)  # корр.счёт
    account_number = models.CharField(max_length=64, blank=True, null=True)  # номер счёта
    account_title = models.CharField(max_length=256, blank=True, null=True)  # наименование счёта

    # юридический адрес
    legal_address_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    legal_address_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    legal_address_city = models.ForeignKey(City, on_delete=models.PROTECT)
    legal_address_postcode = models.CharField(max_length=16)
    legal_address_info = models.CharField(max_length=256)
    # фактический адрес
    fact_address_country = models.ForeignKey(Country, on_delete=models.PROTECT)
    fact_address_region = models.ForeignKey(Region, on_delete=models.PROTECT)
    fact_address_city = models.ForeignKey(City, on_delete=models.PROTECT)
    fact_address_postcode = models.CharField(max_length=16)
    fact_address_info = models.CharField(max_length=256)
