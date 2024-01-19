from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, "home.html")

def about(request):

    return HttpResponse("<h5>This is about page</h5>")

def loginPage(request):

    return render(request, "login.html")
