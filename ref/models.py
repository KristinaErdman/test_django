from django.db import models


class TestModel(models.Model):
    name = models.CharField(verbose_name='name', max_length=50)
