from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InstaLetterRecipient(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()

class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    profile = models.ForeignKey(User,null=True)
    likes = models.CharField(max_length=50)
    comments = models.CharField(max_length=50)

    def __str__(self):
        return self.image_name

class Profile(models.Model):
    bio = models.CharField(max_length=50)        
    user = models.IntegerField(default=0)
    
    def __str__(self):
        return self.bio
