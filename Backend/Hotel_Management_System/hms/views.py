from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from hms.models import Bookings, Rooms_details


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

def gallery (request):
    return render(request, 'gallery.html')

def signup (request):
    if not request.user.is_anonymous: #works when user is logged in 
        return redirect("/")
    if request.method=="POST":

        User = get_user_model()
        users = User.objects.all()
        user_list=[]
        email_list=[]
        for i in users:
            user_list.append(i.username)
            email_list.append(i.email)

        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if email in email_list:
            messages.error(request, 'Email already signed up. Head to login page.')
            return render(request,'signup.html')
        
        if name in user_list:
            messages.error(request, 'Username already Taken. Please try something else.')
            return render(request,'signup.html')
        
        user = User.objects.create_user(username=name, email=email, first_name=name, password=password)
        user.save()
        messages.success(request, f'Your account is created {name}. Head to login page!')
    
    return render(request, 'signup.html')

def signin (request):
    if not request.user.is_anonymous:
            return redirect('/')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('/booking')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request,'signin.html')
    return render(request, 'signin.html')

def signout (request):
    logout(request)
    return redirect('/signin')


def booking_verification (request):

    if request.method=='POST':
        checkin=request.POST.get('checkin')
        checkout=request.POST.get('checkout')
        Rooms=request.POST.get('Rooms')
        guest_count=int(request.POST.get('guest_count'))
        username=str(request.user.username)
        booking_ID=Bookings.objects.count()

       # room_price=Rooms_details.objects.filter(room_type=Rooms)[0].price
        dic={'checkin':checkin, 'checkout':checkout, 'roomtype':Rooms, 'guest_count':guest_count, 'price_per_night': Rooms, 'username':username, 'totalprice':0}
        return render(request, 'booking_verification.html', dic)
    
    return render(request, 'booking_verification.html')