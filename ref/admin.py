from django.contrib import admin
from django.contrib.admin import register

from .models import TestModel


@register(TestModel)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name',)
