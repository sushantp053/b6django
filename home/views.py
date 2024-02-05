import datetime
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from home.models import *
import json

@login_required
def home(request):

    # post = Post.objects.all().order_by('-posted_at')
    freinds  = Friend.objects.filter(user = request.user.id)
    likes = Like.objects.filter(user_id = request.user.id)
    likedPostId = [i.post_id.post_id for i in likes]
    print(likedPostId)
    post = Post.objects.filter(user_id__in = [i.friend for i in freinds]+[request.user.id]).order_by('-posted_at')
    # post = Post.objects.filter(user_id = request.user.id).order_by('-posted_at')
    p = {'posts': post, 'likes': likedPostId}
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
        # imag = request.FILES.get('image')
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


def addFriend(request):

    if(request.method == "POST"):
        try:
            data = json.loads(request.body)
            fid = data.get('id')
            Friend.objects.create(user = User.objects.get(pk = request.user.id), friend = User.objects.get(pk = fid))
            return JsonResponse({'message': 'Friend added successfully'})
        except Exception as e:
            return JsonResponse({'message': f'Error deleting item: {str(e)}'}, status=500)
    

    if(request.method == "GET"):

        freinds  = Friend.objects.filter(user_id = request.user.id)

        notFriend = User.objects.exclude( id__in = [i.friend_id for i in freinds]+[request.user.id])

        print(notFriend)

        return render(request, "addFriend.html" , {'freinds': freinds, 'notFriend': notFriend})

    return render(request, "addFriend.html")

def post(request, post_id):
    post = Post.objects.get(pk = post_id)
    comments = Comments.objects.filter(post_id = post_id).order_by('-commented_at')
    return render(request, "post.html", {'post': post, 'comments': comments})

def comment(request, post_id):
    if(request.method == "POST"):
        comment = request.POST.get('text')
        user = request.user
        post = Post.objects.get(pk = post_id)
        Comments.objects.create(comment = comment, user_id = user, post_id = post, commented_at= datetime.datetime.now())
        return redirect("/post/"+ str(post_id))
    

def likePost(request):

    if(request.method == "POST"):
        # try:
            data = json.loads(request.body)
            pid = data.get('postid')
            try:
                like = Like.objects.get(post_id = Post.objects.get(pk = pid, user_id = User.objects.get(pk = request.user.id)))
                like.delete()
                return JsonResponse({'message': 'Post unliked successfully'})
            except Exception as e:
                Like.objects.create(post_id = Post.objects.get(pk = pid), user_id = User.objects.get(pk = request.user.id), liked_at= datetime.datetime.now())
                return JsonResponse({'message': 'Post liked successfully'})
        # except Exception as e:
        #     return JsonResponse({'message': f'Error: {str(e)}'}, status=500)