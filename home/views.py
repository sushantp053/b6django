import datetime
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import *

@login_required
def home(request):

    # post = Post.objects.all().order_by('-posted_at')
    post = Post.objects.filter(user_id = request.user.id).order_by('-posted_at')
    p = {'posts': post}
    return render(request, "home.html", context= p)

@login_required
def about(request):

    return HttpResponse("<h5>This is about page</h5>")

def loginPage(request):

    return render(request, "login.html")

def handleLogin(request):

    if(request.method == "POST"):
        userName = request.POST.get('username')
        password = request.POST.get('password')
        print(userName, password)

        user = authenticate(username=userName, password=password)
        if user:
            # User is authenticated
            login(request,user)
            return redirect("/home")
            # post = Post.objects.filter(user_id = request.user.id).order_by('-posted_at')
            # p = {'posts': post}
            
            # return render(request, "home.html", p)
        else :
            message = {"error": "Invalid Credintials"}
            return render(request, "login.html", context= message)
        
    return render(request, "error.html")

def logoutUser(request):
    logout(request)
    return render(request, "login.html")

@login_required
def createPost(request):

    if(request.method == "POST"):
        img = request.FILES['image']
        text = request.POST.get('text')
        location = request.POST.get('location')

        post = Post()
        post.image = img
        post.text = text
        post.user_id = request.user
        post.posted_at = datetime.datetime.now()
        post.location = location
        post.save()
        # p1 = Post(
        #     image = img,
        #     text = text,
        #     user_id = request.user,
        #     posted_at = datetime.now(),
        #     location = location
        # )
        # p1.save()

        return redirect("home")
    
    if(request.method == "GET"):
        return render(request, "createPost.html")

    return render(request, "createPost.html")


