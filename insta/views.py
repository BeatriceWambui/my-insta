from django.shortcuts import render,redirect
from django.http import Http404,HttpResponseRedirect
from .models import Image,Profile
from django.contrib.auth.models import User
from .email import send_email
from django.contrib.auth.decorators import login_required
from .models import CommentFormRecipient
from .forms import InstaForm,CommentForm,ImageUploadForm,UploadProfileForm

# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    current_user =request.user
    comments = CommentFormRecipient.objects.all()
    commentform =CommentForm()
    post = Image.images_all()
    profile = Profile.objects.all()
    users = Profile.objects.all()
    following = User.objects.all().exclude(id=request.user.id)
    return render(request,'blueprint/index.html',{'post':post,'comments':comments,'profile':profile,'users':users,'following':following,'commentform':commentform})


@login_required(login_url='/accounts/register/')
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
    return render(request,'blueprint/index.html',{'instaForm':form})

def search_results(request):
    if 'post' in request.GET and request.GET['post']:
        search_term = request.GET.get('post')
        searched_posts = Image.search_by_image_name(search_term)
        message = f'{search_term}'

        return render(request,'templates/search.html',{'message':message,'post':searched_posts})
    else:
        message = 'What you searched for does not exist'
        return render(request,'search.html',{'message':message})

def profile(request):
    current_user=request.user
    post=Image.objects.filter(profile_id=current_user.id)
    form = UploadProfileForm()
    return render(request,'blueprint/profile.html',{'post':post,'forms':form})

def comment(request):
    if request.method == 'POST':
        myform=CommentForm(request.POST)
        if myform.is_valid():
            comment = myform.cleaned_data['comment']
            recipient = CommentFormRecipients(comment=comment)
            recipient.save()
            HttpResponseRedirect('index')
    else:
            myform = CommentForm()
    return render(request,'blueprint/index.html',{'myform':myform})

@login_required(login_url='/accounts/register/')
def likePost(request,image_id):

        image = Image.objects.get(pk = image_id)

        if image.likes.filter(id = request.user.id).exists():
            image.likes.remove(request.user)
            is_liked = False
        else:
            image.likes.add(request.user)
            is_liked = True

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/accounts/register/')
def upload(request):
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_name = form.cleaned_data['image_name']
            image_caption = form.cleaned_data['image_caption']
            current_user = request.user
            saveImage = Image(image=image,image_name=image_name,image_caption=image_caption,profile=current_user)
            saveImage.save()
            return redirect(index)
    else:
        form = ImageUploadForm()
        return render(request,'blueprint/upload.html',{'form':form})
            
def uploadProfile(request):   
    if request.method == 'POST':
        forms = UploadProfileForm(request.POST,request.FILES)
        if forms.is_valid():
            profile_image=form.cleaned_data['profile_image']
            saveProfile  = Profile(profile_image=profile_image)
            saveProfile.save()
            return redirect(index)
    else:
        forms=UploadProfileForm()
        return render(request,'blueprint/profile.html',{'forms':forms})

