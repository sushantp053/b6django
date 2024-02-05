
from django.contrib import admin
from django.urls import path
from b6django import settings
from django.conf.urls.static import static
import home.views
from home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("login/", loginPage, name="login"),
    path('loginUser', handleLogin),
    path('logoutUser', logoutUser),
    path('createPost', createPost),
    path('register', register),
    path('error', error),
    path('addFriend', addFriend),
    path('post/<int:post_id>', post),
    path('comment/<int:post_id>', comment),
    path('likePost', likePost),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
