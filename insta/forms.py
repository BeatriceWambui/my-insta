from django import forms

class InstaForm(forms.Form):
    first_name = forms.CharField(label='First Name',max_length=30)
    second_name = forms.CharField(label='Last Name',max_length=30)
    email = forms.EmailField(label='Email')