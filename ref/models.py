from django.db import models

from test_django.utils import BaseModel, BaseSingleton


class TestModel(BaseModel):
    name = models.CharField(verbose_name='name', max_length=50)


class Page(BaseSingleton):
    title = models.CharField(verbose_name='title', max_length=200)
    description = models.TextField(verbose_name='text')
