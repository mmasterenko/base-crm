from django.db import models
from django.conf import settings

from core.models import Account


class AccountMixin(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CreatorMixin(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
