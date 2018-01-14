from django.db import models

from utils.model_mixin import CreateUpdateMixin


class Organisation(CreateUpdateMixin, models.Model):
    pass


class Shop(CreateUpdateMixin, models.Model):
    pass


class CounterAgent(CreateUpdateMixin, models.Model):
    """
    контрагент - может быть ИП, ООО, физ.лицо и т.д.
    """
    pass
