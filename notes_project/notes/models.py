from django.db import models
from user.models import User

class Note(models.Model):
    note_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,related_name='notes', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    create_time = models.CharField(max_length=200)
    version = models.IntegerField(default=0)
    folder = models.ForeignKey('Folder', related_name='notes', on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    TEXT = 0
    AUDIO = 1
    IMAGE = 2

    CONTENT_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (IMAGE, 'Image')
    ]

    note_id = models.ForeignKey(Note, related_name='contents', on_delete=models.CASCADE)
    content_id = models.IntegerField(primary_key=True)
    content_type = models.IntegerField(choices=CONTENT_TYPES)
    text = models.TextField(blank=True, null=True)
    file_url =models.CharField(max_length=200,blank=True)
    file = models.FileField(upload_to='uploads/',blank=True)
    position = models.IntegerField()
    version = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.note.title} - {self.content_type}"
    
class Folder(models.Model):
    folder_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User,related_name='folders', on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=200)
    version = models.IntegerField(default=0)

    def __str__(self):
        return self.folder_name