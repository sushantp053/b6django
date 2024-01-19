
from django.contrib import admin
from django.urls import path
import home.views
from home.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("home", home, name="home"),
    path("about", about, name="about"),
    path("login", loginPage, name="login"),
]
