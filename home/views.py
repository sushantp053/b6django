from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):

    return render(request, "home.html")

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
            return render(request, "home.html")
        else :
            message = {"error": "Invalid Credintials"}
            return render(request, "login.html", context= message)
        
    return render(request, "error.html")

def logoutUser(request):
    logout(request)
    return render(request, "login.html")

    

