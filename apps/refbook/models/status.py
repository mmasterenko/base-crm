from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class OrderStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    статус заказа
    """
    title = models.CharField(max_length=64)
    is_for_new_orders = models.BooleanField(default=True)

    class Meta:
        db_table = 'order_status'


class TaskStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'task_status'


class CustomerRequestStatus(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    статус обращения
    """
    title = models.CharField(max_length=64)

    class Meta:
        db_table = 'request_status'
