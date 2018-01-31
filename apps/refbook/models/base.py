from django.db import models
from django.conf import settings

from core.models import Country, Region, City
from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from .choices import CURRENCY_TYPE, PROPERTY_TYPE
from .type import PriceType


class CashBox(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    касса
    """
    title = models.CharField(max_length=128)
    organisation = models.ForeignKey('refbook.Organisation', on_delete=models.PROTECT)
    currency = models.PositiveSmallIntegerField(choices=CURRENCY_TYPE, default=0)
    notes = models.CharField(max_length=512)


class BankAccount(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    расчетный счет
    """
    title = models.CharField(max_length=128)
    organisation = models.ForeignKey('refbook.Organisation', on_delete=models.PROTECT)
    currency = models.PositiveSmallIntegerField(choices=CURRENCY_TYPE, default=0)
    notes = models.CharField(max_length=512)
    # банковские реквизиты
    bik = models.CharField(max_length=64, blank=True, null=True, unique=True)  # БИК
    bank_title = models.CharField(max_length=256, blank=True, null=True)  # название банка
    korr_account = models.CharField(max_length=64, blank=True, null=True)  # корр.счёт
    account_number = models.CharField(max_length=64, blank=True, null=True)  # номер счёта
    account_title = models.CharField(max_length=256, blank=True, null=True)  # наименование счёта


class Organisation(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    организации
    """
    DOCUMENT_PREFIX_TYPE = (
        (0, 'в начале месяца'),
        (1, 'в начале года'),
    )

    title = models.CharField(max_length=128)
    property_type = models.PositiveSmallIntegerField(choices=PROPERTY_TYPE)
    # реквизиты
    inn = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ИНН
    kpp = models.CharField(max_length=64, blank=True, null=True, unique=True)  # КПП
    ogrn = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ОГРН
    okpo = models.CharField(max_length=64, blank=True, null=True, unique=True)  # ОКПО
    # данные по организации
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    notes = models.CharField(max_length=512)
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
    # настройки учета
    vat = models.PositiveSmallIntegerField(default=0)  # НДС (value-added tax)
    selling_price_default_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    purchase_price_default_type = models.ForeignKey(PriceType, on_delete=models.PROTECT)
    # префикс к номерам документов
    prefix_type = models.PositiveSmallIntegerField(choices=DOCUMENT_PREFIX_TYPE)
    prefix_string = models.CharField(max_length=16)
    prefix_places = models.PositiveSmallIntegerField(null=True, blank=True)  # число знаков
    # подпись и печать
    chief = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    chief_position = models.CharField(max_length=128)
    chief_signature = None  # img
    accountant = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL)
    accountant_signature = None  # img
    organisation_seal = None  # img
    default_bank_account = models.OneToOneField(BankAccount, blank=True, null=True,
                                                on_delete=models.SET_NULL)  # расчетный счет по-умолчанию
    default_cashbox = models.OneToOneField(CashBox, blank=True, null=True,
                                           on_delete=models.SET_NULL)  # касса по-умолчанию


class Shop(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    pass
