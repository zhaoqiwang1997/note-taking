from django.contrib import admin
from notetaking.models import Tag, Note

admin.site.site_header = 'Note taking system'
admin.site.index_title = 'Notes'
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Note)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'date']
