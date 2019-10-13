from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from .forms import InstaForm
from .email import send_email
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
  
    return render(request,'blueprint/index.html')
@login_required(login_url='/accounts/login/')
def mysubscribe(request):
    if request.method == 'POST':
        form = InstaForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            recipient = InstaLetterRecipient(first_name=first_name,second_name=second_name,email=email)
            recipient.save()
            send_email(first_name,second_name,email)
            HttpResponseRedirect('mysubscribe')
        
    else:
        form = InstaForm()
    return render(request,'blueprint/index.html.html',{'instaForm':form})
