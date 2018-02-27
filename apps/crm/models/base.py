from django.db import models
from django.conf import settings
from django.utils import timezone

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin
from apps.refbook.models import (Organisation, Shop, OrderingMethod, OrderingSource,
                                 CounterAgent, TaskStatus, CustomerRequestStatus)


class Task(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    задачи
    """
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    text = models.TextField()
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsible_for_tasks',
                                    on_delete=models.PROTECT)
    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)
    base_on_ref = None  # (документ основание) ссылка на другую сущность: Заказы, Обращение и т.д.

    class Meta:
        db_table = 'task'


class CustomerRequest(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    обращения пользователей
    """
    datetime = models.DateTimeField(default=timezone.now)

    status = models.ForeignKey(CustomerRequestStatus, on_delete=models.PROTECT)  # статус
    ordering_source = models.ForeignKey(OrderingSource, on_delete=models.PROTECT)  # источник оформления
    ordering_method = models.ForeignKey(OrderingMethod, on_delete=models.PROTECT)  # тип оформления

    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsible_for_customer_requests',
                                    on_delete=models.PROTECT)
    text = models.TextField()  # цель обращения

    counter_agent = models.ForeignKey(CounterAgent, on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    class Meta:
        db_table = 'request'


class VoiceCall(AccountMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    звонки
    """
    datetime = models.DateTimeField(default=timezone.now)
    ordering_source = models.ForeignKey(OrderingSource, on_delete=models.PROTECT)  # источник оформления
    shop = models.ForeignKey(Shop, on_delete=models.PROTECT)
    responsible = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='responsible_for_voice_calls',
                                    on_delete=models.PROTECT)
    organisation = models.ForeignKey(Organisation, on_delete=models.PROTECT)

    class Meta:
        db_table = 'voice_call'
