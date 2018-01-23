from django.db import models

from project.utils.model_mixin import AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin


class Organisation(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    pass


class Shop(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    pass


class CounterAgent(AccountMixin, CreatorMixin, CreateUpdateMixin, ArchiveMixin, models.Model):
    """
    контрагент - может быть ИП, ООО, физ.лицо и т.д.
    """
    pass
