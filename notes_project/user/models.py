from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    signatrue = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    image = models.FileField(upload_to='uploads/',blank=True)
    version = models.IntegerField(default=0)