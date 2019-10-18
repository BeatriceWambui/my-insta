from django import forms
from .models import CommentFormRecipient,Image,Profile

class InstaForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=30)
    second_name = forms.CharField(label='Last Name',max_length=30)
    email = forms.EmailField(label='Email')

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentFormRecipient
        fields=('comment',)

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Image
        fields=['image','image_name','image_caption']

class UploadProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_image','bio']
        