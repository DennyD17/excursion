from django.contrib import admin
from . import models


class ChoiceInline(admin.StackedInline):
    model = models.ExcursionImageStorage
    extra = 2


class ExcursionAdmin (admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ChoiceInline]


class BlogImgInline(admin.StackedInline):
    model = models.BlogImageStore
    extra = 2


class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImgInline]


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


class PeopleTable(admin.ModelAdmin):
    list_display = ('event', 'date', 'name', 'email', 'phone')
    ordering = ('-date',)


admin.site.register(models.About, OneNoteAdmin)
admin.site.register(models.Contacts, OneNoteAdmin)
admin.site.register(models.Excursion, ExcursionAdmin)
admin.site.register(models.PeopleReg, PeopleTable)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogImageStore)
admin.site.register(models.ExcursionImageStorage)
