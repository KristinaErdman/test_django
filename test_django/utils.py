from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models


class BaseModel(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    # вместо:
    objects = models.Manager()
    on_site = CurrentSiteManager()

    # можно сделать так:
    # objects = CurrentSiteManager()
    # тогда в админке в зависимости от сайта будут видны только соответствующие записи
    # и не нужно будет ничего править в коде старых контроллеров

    class Meta:
        abstract = True
