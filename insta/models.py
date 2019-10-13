from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.

class InstaLetterRecipient(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()

class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='picture/',null=True)
    bio = HTMLField()
    username = models.CharField(max_length=30,blank=True)
    user_id = models.IntegerField(default=0)
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

