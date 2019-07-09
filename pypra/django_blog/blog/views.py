from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users, Articles, Album, Leave
import hashlib
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(
        request,
        'blog/login.html'
    )

#????????????????????
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if username != None and password != None:
            md = hashlib.md5()
            md.update(password.encode('utf-8'))
            spasswd = md.hexdigest()
            user = Users.objects.filter(username=username, password=spasswd)
            if user:
                return redirect('/index/')
    return render(
        request,
        'blog/login.html'
    )

#???????????????????
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        if username != None and password != None:
            md = hashlib.md5()
            md.update(password.encode('utf-8'))
            spasswd = md.hexdigest()
            newuser = Users(username=username, password=spasswd)
            newuser.save()
            return redirect('/login/')
    else:
        return render(
            request,
            'blog/signup.html'
        )

def index(request):
    article_li = Articles.objects.all()
    paginator = Paginator(article_li, 2)
    page = request.GET.get('page', 1)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', {'articles': articles})

def album(request):
    album_li = Album.objects.all()
    paginator = Paginator(album_li, 4)
    page = request.GET.get('page', 1)
    try:
        albums = paginator.page(page)
        print(albums.number)
    except PageNotAnInteger:
        albums = paginator.page(1)
        print(albums.number)
    except EmptyPage:
        albums = paginator.page(paginator.num_pages)
        print(albums.number)
    return render(request, 'blog/album.html', {'albums': albums})

def thoughts(request):
    return render(
        request,
        'blog/thoughts.html'
    )


def comments(request):
    comment_li = Leave.objects.all()
    paginator = Paginator(comment_li, 7)
    page = request.GET.get('page', 1)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)
    return render(request, 'blog/comments.html', {'comments': comments})