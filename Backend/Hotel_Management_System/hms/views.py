from django.shortcuts import render, HttpResponse


# Create your views here.
def index (request):
    return HttpResponse("This is homepage")

def about (request):
    return HttpResponse("This is about")

def rooms (request):
    return HttpResponse("This is rooms")

def blogs (request):
    return HttpResponse("This is blogs")

def offers (request):
    return HttpResponse("This is offers")