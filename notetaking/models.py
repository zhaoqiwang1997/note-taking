from django.db import models
from datetime import date

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    date = models.DateField(default=date.today)
    content = models.TextField()
