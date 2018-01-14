from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from utils.model_mixin import CreateUpdateMixin


class Account(CreateUpdateMixin, models.Model):

    owner = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='my_account',
                                 on_delete=models.PROTECT)


class User(CreateUpdateMixin, AbstractUser):
    """
    customized User model
    """
    account = models.ForeignKey(Account, null=True, on_delete=models.PROTECT)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
