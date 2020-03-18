from django.shortcuts import render
from .models import Post
from django.views import generic
from .forms import *
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect,render,get_object_or_404,reverse
# Create your views here.
def postview(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})



#class PostDetail(generic.DetailView):
    #model = Post
    #template_name = 'postdet.html'

def PostDetail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    #response.increase()
    #comments= Comment.objects.filter(post=post).order_by('-created_date')



    return render(request, 'postdet.html', {'post': post})

@login_required(login_url='login')
def writepost(request):
    if request.method == "POST":
        form = writeblog(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(user_id=request.user.pk)
            return redirect('postview')
    else:
        form = writeblog()
    return render(request, 'writeup.html',{'form':form})


def blogbyauthor(request):
    query=request.GET['author']
    author= get_object_or_404(User, username=query)#this is needed when we apply search filter to foreign key
    posts = Post.objects.filter(author=author.id).order_by('-created_on')
    #paginator = Paginator(responses, 10) # Show 10 responses per page
    #page = request.GET.get('page')
    #posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})


#def signup(request):
    #if request.method == 'POST':
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        username = form.cleaned_data.get('username')
    #        raw_password = form.cleaned_data.get('password')
    #        user = authenticate(username=username, password=raw_password)
    #        login(request, user)
    #        return redirect('postview')
    #else:
    #    form = UserCreationForm()
    #return render(request, 'register.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('postview')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    _message = False
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('postview')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('postview')
