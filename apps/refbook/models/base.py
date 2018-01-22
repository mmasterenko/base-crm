from django.db import models

from utils.model_mixin import CreateUpdateMixin
from project.utils.model_mixin import AccountMixin, CreatorMixin


class Organisation(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    pass


class Shop(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    pass


class CounterAgent(AccountMixin, CreatorMixin, CreateUpdateMixin, models.Model):
    """
    контрагент - может быть ИП, ООО, физ.лицо и т.д.
    """
    pass
