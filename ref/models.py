from django.db import models

from test_django.utils import BaseModel


class TestModel(BaseModel):
    name = models.CharField(verbose_name='name', max_length=50)
