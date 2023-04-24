from rest_framework import serializers
from notetaking.models import Tag, Note, Folder

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['name']

    def update (self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

    def update (self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

class NoteSerializer(serializers.ModelSerializer):
    folder = FolderSerializer()
    tag = TagSerializer()
    class Meta:
        model = Note
        fields = ['title']
        fields = ['title', 'date', 'tag', 'folder', 'content']

    # def create(self, validated_data):
    #     # Create and return a new MyModel instance using the validated data
    #     return Note.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        
        # Update folder and tag objects
        folder_data = validated_data.pop('folder', None)
        tag_data = validated_data.pop('tag', None)
        folder_serializer = self.fields['folder']
        tag_serializer = self.fields['tag']

        if folder_data:
            folder_instance = instance.folder
            folder = folder_serializer.update(folder_instance, folder_data)
            validated_data['folder'] = folder
        
        if tag_data:
            tag_instance = instance.tag
            tag = tag_serializer.update(tag_instance, tag_data)
            validated_data['tag'] = tag
        
        instance.save()
        return instance