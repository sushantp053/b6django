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

def error(request):
    return render(request, "error.html")

def register(request):
    if(request.method == "POST"):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        phone = request.POST.get('phone')

        if password == confirmPassword:
            try:
                user = User.objects.create_user(userName, email, password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
            except Exception as e:
                print(e)
                user = {"error": "Username already exists",
                    "firstname": firstname, 
                    "lastname" : lastname,
                    "email" :email, 
                    "phone" : phone}
                return render(request, "register.html", context = user)

            profile = Profile.objects.create(user_id = user)
            profile.phone = phone
            profile.save()

            return redirect("login")
        else:
            user = {"error": "Password and Confirm Password does not match",
                    "firstname": firstname, 
                    "lastname" : lastname,
                    "username" : userName, 
                    "email" :email, 
                    "phone" : phone}
        
            return render(request, "register.html", context = user)

    elif(request.method == "GET"):
        return render(request, "register.html")
    else:
        return redirect("/error")

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
