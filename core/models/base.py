from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from project.utils.model_mixin import CreateUpdateMixin, ArchiveMixin


class Account(CreateUpdateMixin, models.Model):
    """
    The main unit of the service
    """
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='my_account',
                                 on_delete=models.PROTECT)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=False)
    trial_till = models.DateTimeField()


class User(CreateUpdateMixin, ArchiveMixin, AbstractUser):
    """
    customized User model
    """
    account = models.ForeignKey(Account, null=True, on_delete=models.PROTECT)
    phone = models.CharField(max_length=16, blank=True, null=True)
    patronymic_name = models.CharField(max_length=32, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=128, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
