from django.db import models


class Country(models.Model):
    """
    лучше не использовать модели из других пакетов без необходимости.
    чем больше контроля будет у меня, тем лучше
    """
    pass  # посмотреть пакет django-countries

    class Meta:
        db_table = 'geo_country'


class Region(models.Model):
    pass

    class Meta:
        db_table = 'geo_region'


class City(models.Model):
    pass

    class Meta:
        db_table = 'geo_city'
