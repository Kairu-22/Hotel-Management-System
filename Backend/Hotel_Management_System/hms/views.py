from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User


# Create your views here.
def Welcome (request):
    return render(request, 'Welcome.html')

def rooms (request):
    return render(request, 'room_details.html')

def booking (request):
    return render(request, 'Booking.html')

def blogs (request):
    return render(request, 'blogs_reviews.html')

def offers (request):
    return render(request, 'offers.html')

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