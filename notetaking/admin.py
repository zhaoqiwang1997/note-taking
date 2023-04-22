from django.contrib import admin
from notetaking.models import Tag, Note, Folder
from django.urls import reverse
from django.utils.html import format_html
from urllib.parse import urlencode

admin.site.site_header = 'Note taking system'
admin.site.index_title = 'Notes'
# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'note_count']

    @admin.display(ordering='note_count')
    def note_count(self, tag):
        numbers = Note.objects.filter(tag=tag).count()
        url = (
            reverse('admin:notetaking_note_changelist')
            + '?'
            + urlencode({
                'tag__id': tag.id
            }))
        return format_html('<a href="{}">{} Note(s)</a>', url, numbers)
    
    # Set a custom column name for the note count
    note_count.short_description = 'Number of Notes'

@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['name', 'note_count']

    @admin.display(ordering='note_count')
    def note_count(self, folder):
        numbers = Note.objects.filter(folder=folder).count()
        url = (
            reverse('admin:notetaking_note_changelist')
            + '?'
            + urlencode({
                'folder__id': folder.id
            }))
        return format_html('<a href="{}">{} Note(s)</a>', url, numbers)
    
    # Set a custom column name for the note count
    note_count.short_description = 'Number of Notes'

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'folder', 'tag', 'date']