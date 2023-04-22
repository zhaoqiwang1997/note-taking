from django.db import models
from datetime import date

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)
    featured_note = models.ForeignKey(
        'Note', on_delete=models.SET_NULL, null=True, related_name='tags', blank=True)

    def __str__(self) -> str:
        return self.name
class Folder(models.Model):
    name = models.CharField(max_length=50)
    classified_note = models.ForeignKey(
        'Note', on_delete=models.SET_NULL, null=True, related_name='folders', blank=True)


    def __str__(self) -> str:
        return self.name
class Note(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    tag = models.ForeignKey(
        'Tag', on_delete=models.SET_NULL, null=True, related_name='notes_in_tag', blank=True)
    folder = models.ForeignKey(
        'Folder', on_delete=models.SET_NULL, null=True, related_name='notes_in_folder', blank=True)
    content = models.TextField()
