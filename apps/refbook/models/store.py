from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class Warehouse(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    склад
    """
    WRITE_OFF_TYPE = (
        (0, 'списание по FIFO'),
        (1, 'списание по среднему'),
    )
    title = models.CharField(max_length=64)
    write_off = models.PositiveSmallIntegerField(choices=WRITE_OFF_TYPE)
    address = models.CharField(max_length=256)
    notes = models.TextField()
