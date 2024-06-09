# serializers.py
from .models import Note, Content

from django import forms
from .models import Note, Content

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note_id','user_id', 'title','create_time','version']
    def validate_unique(self) -> None:
        pass

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['note_id','content_id', 'content_type', 'text','file','file_url', 'position','version']
    def validate_unique(self) -> None:
        pass
