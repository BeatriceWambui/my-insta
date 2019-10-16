from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class InstaLetterRecipient(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    email = models.EmailField()

class Image(models.Model):
    image =models.ImageField(upload_to ='photos/',null=True)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)
    profile = models.ForeignKey(User,null=True)
    likes = models.CharField(max_length=50)
    comments = models.CharField(max_length=50, null=True)
      
    @classmethod
    def images_all(cls):
        post = Image.objects.all()
        return post

    @classmethod
    def search_by_image_name(cls,search_term):
        insta = cls.objects.filter(title__icontains=search_term)
        return insta

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Profile(models.Model):
    profile_image = models.ImageField(upload_to='photos/',null=True,default ='default.jpg')
    bio = models.CharField(max_length=50)        
    username = models.OneToOneField(User,unique = True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username.username} Profile'
    def save_profile(self):
        self.save()
 

class CommentFormRecipient(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Image,on_delete=models.CASCADE,related_name='comment')
    username = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='comment')
    
    def __str__(self):
        return self.comment

