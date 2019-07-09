from django.urls import path
from blog import views
from django.views.static import serve


urlpatterns = [
    path("", views.home, name="home"),
    path("blog/index", views.index, name="index"),
    path("blog/album", views.album, name="album"),
    path("blog/thoughts", views.album, name="thought"),
    path("blog/comments", views.comments, name="comments"),
    path("blog/login", views.login, name="login"),
    path("blog/signup", views.signup, name="signup"),
    path("thoughts/", views.thoughts, name="thoughts"),
    path("index/", views.index, name="index"),
    path("comments/", views.comments, name="comments"),
    path("album/", views.album, name="album"),
    path("index/", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("media/(?P<path>.*)$", serve),
]