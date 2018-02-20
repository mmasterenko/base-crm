from django.db import models
from django.conf import settings


class AccountMixin(models.Model):
    account = models.ForeignKey('core.Account', on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CreatorMixin(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class ArchiveMixin(models.Model):
    is_archive = models.BooleanField(default=False)

    class Meta:
        abstract = True


class CreateUpdateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
