from django.contrib import admin
from .models import Image,Profile,InstaLetterRecipient,CommentFormRecipient
# Register your models here.

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(InstaLetterRecipient) 
admin.site.register(CommentFormRecipient)