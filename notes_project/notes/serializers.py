from rest_framework import serializers
from .models import Note, Content,Folder

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['note_id','content_id', 'content_type', 'text','file', 'file_url', 'position','version']

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = ['note_id','user_id' ,'title', 'create_time','version']

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = ['folder_name','folder_id','user_id', 'version']