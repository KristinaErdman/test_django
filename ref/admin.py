from django import forms
from django.conf import settings
from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m
from django.contrib.sites.models import Site
from django.db import router, transaction

from .models import TestModel, Page


class BaseForm(forms.ModelForm):
    def get_initial_for_field(self, field, field_name):
        if field_name == 'site':
            field.queryset = Site.objects.filter(pk=settings.SITE_ID)
            return settings.SITE_ID
        return super().get_initial_for_field(field, field_name)


class BaseModelAdmin(admin.ModelAdmin):
    form = BaseForm

    def get_queryset(self, request):
        qs = self.model.on_site.get_queryset()
        ordering = self.get_ordering(request)
        if ordering:
            qs = qs.order_by(*ordering)
        return qs


class BaseSingletonAdmin(admin.ModelAdmin):
    form = BaseForm

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        try:
            obj = self.model.on_site.get()
        except self.model.DoesNotExist:
            obj = self.model.objects.create(site_id=settings.SITE_ID)
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._changeform_view(request, str(obj.pk), form_url='', extra_context=extra_context)


@admin.register(TestModel)
class TestAdmin(BaseModelAdmin):
    list_display = ('name',)


@admin.register(Page)
class PageAdmin(BaseSingletonAdmin):
    list_display = ('title', 'description')
