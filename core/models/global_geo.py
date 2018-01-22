from django.db import models


class Country(models.Model):
    pass  # посмотреть пакет django-countries
    """
    лучше не использовать модели из других пакетов без необходимости.
    чем больше контроля будет у меня, тем лучше
    """


class Region(models.Model):
    pass


class City(models.Model):
    pass
