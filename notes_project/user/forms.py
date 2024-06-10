from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id', 'password', 'username','signatrue','image_url','image','version'] 
    def validate_unique(self) -> None:
        pass