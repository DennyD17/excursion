from django.contrib import admin
from . import models


class ExcursionAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class OneNoteAdmin (admin.ModelAdmin):

    def has_add_permission(self, request):
        qs = super(OneNoteAdmin, self).get_queryset(request)
        num = qs.count()
        if num > 0:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        return False


class Filter(admin.ModelAdmin):
    list_filter = ('name', )


admin.site.register(models.About, OneNoteAdmin)
admin.site.register(models.Contacts, OneNoteAdmin)
admin.site.register(models.Event, Filter)
admin.site.register(models.Excursion, ExcursionAdmin)
admin.site.register(models.ImportantNote)
