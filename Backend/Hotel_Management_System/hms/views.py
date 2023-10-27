from django.shortcuts import render, HttpResponse


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
    return render(request, 'signin.html')

def signup (request):
    return render(request, 'signup.html')