from rest_framework import serializers
from notetaking.models import Tag, Note, Folder

class NoteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    date = serializers.DateField()

    # def create(self, validated_data):
    #     # Create and return a new MyModel instance using the validated data
    #     return MyModel.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     # Update and return the existing MyModel instance using the validated data
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.save()
    #     return instance
