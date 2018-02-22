from django.db import models
from django.conf import settings


class AccountMixin(models.Model):
    account = models.ForeignKey('core.Account',
                                verbose_name='аккаунт',
                                help_text='аккаунт, которому принадлежит запись',
                                on_delete=models.CASCADE)

    class Meta:
        abstract = True


class CreatorMixin(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='создатель',
                                help_text='пользователь, который создал эту запись',
                                null=True,
                                on_delete=models.SET_NULL)

    class Meta:
        abstract = True


class ArchiveMixin(models.Model):
    is_archive = models.BooleanField('в архиве',
                                     help_text='если этот флаг установлен, запись находится в архиве',
                                     default=False)

    class Meta:
        abstract = True


class CreateUpdateMixin(models.Model):
    created_at = models.DateTimeField('создано',
                                      help_text='время создания записи',
                                      auto_now_add=True)
    updated_at = models.DateTimeField('обновлено',
                                      help_text='время последнего записи',
                                      auto_now=True)

    class Meta:
        abstract = True
