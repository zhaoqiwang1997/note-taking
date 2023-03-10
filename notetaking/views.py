from django.shortcuts import render
from django.http import HttpResponse
from notetaking.models import Tag, Note

# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def createNote(request, tag, title, content):
    obj, created = Tag.objects.get_or_create(
        name=tag,
    )
    if not Note.objects.filter(pk=title).exists():
        Note.objects.create(
            title=title,
            tag=obj,
            content=content
        )
        return HttpResponse("New note created")
    return HttpResponse("Note already exists")