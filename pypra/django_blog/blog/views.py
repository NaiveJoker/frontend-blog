from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(
        request,
        'blog/login.html'
    )

#hello_there page
def hello_there(request, name):
    return render(
        request,
        'blog/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
def index(request):
    return render(
        request,
        'blog/index.html'
    )

def album(request):
    return render(
        request,
        'blog/album.html'
    )

def thoughts(request):
    return render(
        request,
        'blog/thoughts.html'
    )
def login(request):
    return render(
        request,
        'blog/login.html'
    )

def signup(request):
    return render(
        request,
        'blog/signup.html'
    )

def comments(request):
    return render(
        request,
        'blog/comments.html'
    )