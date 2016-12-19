from django.contrib import admin
from . import models


class ExcursionAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.About)
admin.site.register(models.Contacts)
admin.site.register(models.Event)
admin.site.register(models.Excursion, ExcursionAdmin)
admin.site.register(models.ImportantNote)
