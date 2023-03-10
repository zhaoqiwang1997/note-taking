from django.db import models
from datetime import date

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

class Note(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(default=date.today)
    tag = models.ForeignKey(Tag, on_delete=models.PROTECT)
    content = models.TextField()
