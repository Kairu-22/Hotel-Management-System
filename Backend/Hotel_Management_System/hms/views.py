from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User


# Create your views here.
def Welcome (request):
    return render(request, 'Welcome.html')

def rooms (request):
    return HttpResponse("This is rooms")

def blogs (request):
    return HttpResponse("This is blogs")

def offers (request):
    return HttpResponse("This is offers")

def signin (request):
    if request.method=="POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password=password)

        if user is not None:
            return redirect("/")
        else:
            return render(request, "signin.html")
    
    return render(request, 'signin.html')

def signup (request):
    return render(request, 'signup.html')

def signout (request):
    return render(request, 'Welcome.html')