from django.contrib import admin
from django.contrib.admin import register

from .models import TestModel


class MultiDBModelAdmin(admin.ModelAdmin):
    # object_history_template = 'cjhwjbes'

    def save_model(self, request, obj, form, change):
        obj.save(using=request.using_db)

    def delete_model(self, request, obj):
        obj.delete(using=request.using_db)

    def get_queryset(self, request):
        return super().get_queryset(request).using(request.using_db)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=request.using_db, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=request.using_db, **kwargs)


@register(TestModel)
class TestAdmin(MultiDBModelAdmin):
    list_display = ('name',)
