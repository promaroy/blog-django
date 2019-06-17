from django.shortcuts import render
from .models import Post
from django.views import generic
from .forms import writeblog
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect,render,get_object_or_404,reverse
# Create your views here.
def postview(request):
    allposts=Post.objects.all()
    return render(request,'base.html',{'allposts':allposts})



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'postdet.html'

@login_required(login_url='login')
def writepost(request):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            form.save(user_id=request.user.pk)
            return redirect('base')
    else:
        form = ResponseForm()
    return render(request, 'writeup.html', {'form': form})

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
