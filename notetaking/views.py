from django.shortcuts import render
from django.http import HttpResponse
from notetaking.models import Tag, Note, Folder
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from notetaking.serializers import NoteSerializer

# Create your views here.
@api_view(['GET'])
def readNote(request, title):
    try:
        note = Note.objects.get(title=title)
        serializer = NoteSerializer(note)
        return Response({'message': 'Note is found!', 'note': serializer.data})
    except Note.DoesNotExist:
        return Response({'message': 'No such note!'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
def newNote(request):
    if 'title' in request.data:
        if not Note.objects.filter(title=request.data['title']).exists():
            serializer = NoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response({'message': 'Note already exists'}, status=status.HTTP_208_ALREADY_REPORTED)
    return Response({'message': 'Title must be defined!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def updateNote(request, title):
    try:
        note = Note.objects.get(title=title)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Note.DoesNotExist:
        return Response({'message': 'No such note!'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'DELETE'])
def deleteNote(request, title):
    try:
        note = Note.objects.get(title=title)
        serializer = NoteSerializer(note)
        serializer.delete(note)
        return Response(status=status.HTTP_301_MOVED_PERMANENTLY)
    except Note.DoesNotExist:
        return Response({'message': 'No such note!'}, status=status.HTTP_404_NOT_FOUND)

# For Admin site
def hello(request):
    return HttpResponse("Hello world")

def createNote(request, tag, title, content, folder):
    obj_tag = ""
    obj_folder = ""
    if not Tag.objects.filter(pk=tag).exists():
        obj_tag = Tag(name=tag)
        obj_tag.save()
    else:
        obj_tag = Tag.objects.get(name=tag)

    if not Folder.objects.filter(pk=folder).exists():
        obj_folder = Folder(name=folder)
        obj_folder.save()
    else:
        obj_folder = Tag.objects.get(name=tag)

    if not Note.objects.filter(pk=title).exists():
        obj_note = Note(
            title=title,
            tag=obj_tag,
            folder=obj_folder,
            content=content
        )
        obj_note.save()

        obj_tag.notes_in_tag.add(obj_note)
        obj_folder.notes_in_folder.add(obj_note)

        obj_tag.save()
        obj_folder.save()

        return HttpResponse("New note created")
    return HttpResponse("Note already exists")

def getList(request):
    note_list = Note.objects.all()
    titles = []
    for note in note_list:
        titles.append(note.title)
    return HttpResponse(titles)