from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from .forms import InstaForm
from .models import Image,Profile
from django.contrib.auth.models import User
from .email import send_email
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    current_user =request.user
    post = Image.images_all()
    profile = Profile.objects.all()
    users = Profile.objects.all()
    following = User.objects.all().exclude(id=request.user.id)
    return render(request,'blueprint/index.html',{'post':post,'profile':profile,'users':users,'following':following})


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

def search_results(request):
    if 'image_name' in request.GET and request.GET['image_name']:
        search_term = request.GET.get('image_~name')
        searched_post = Image.search_by_image_name(search_term)
        message = f'{search_term}'

        return render(request,'templates/search.html',{'message':message,'post':searched_post})
    else:
        message = 'What you searched for does not exist'
        return render(request,'search.html',{'message':message})

def profile(request):
    current_user=request.user
    post=Image.objects.filter(profile_id=current_user.id)
    return render(request,'blueprint/profile.html',{'post':post,})