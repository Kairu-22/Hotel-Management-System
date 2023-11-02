from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login, get_user_model
from hms.models import Bookings, Rooms_details, Offers
import datetime, re
from functools import reduce
from datetime import date

from json import dumps


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

def dashboard (request):
    booking_list=(Bookings.objects.filter(Username=request.user.username))

    return render(request, 'dashboard.html', {'booking_list':booking_list})

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
        
        
        date1 = date(int(checkin[0:4]), int(checkin[5:7]), int(checkin[8:]))
        date2 = date(int(checkout[0:4]), int(checkout[5:7]), int(checkout[8:]))
        room_price=Rooms_details.objects.filter(room_type=Rooms)[0].price

        numofdays= reduce(lambda x, y: (y-x).days, [date1, date2])
        totalprice=numofdays*room_price

        dic={'checkin':checkin, 'checkout':checkout, 'roomtype':Rooms, 'guest_count':guest_count, 'price_per_night': room_price, 'username':username, 'totalprice':totalprice}
        
        return render(request, 'booking_verification.html', dic)
    
    

    return render(request, 'booking_verification.html')

def booking_confirm(request):
    data = request.GET.get('data').split(',')
    booking_ID="BID"+re.sub(r'[ :-]', '', str(datetime.datetime.now())[:-7])
    print (data)
    BOOK=Bookings(booking_ID=booking_ID, Username=data[2], checkin=data[0], checkout=data[1], room_type=data[3], total_price=1000, guest_count=0 )
    BOOK.save()
    return render (request, 'booking_confirm.html')


def calculatedPrice(room,coupon):
    # Define a dictionary mapping div classes to room prices
    room_prices = {
'room-details kingbed_garden': 8140 ,
'room-details superiorbed_garden':8140,
'room-details kingbed_pool':10187,
'room-details Deluxe':11187,
'room-details Executive':34187,
'room-details Luxury':36846
    }
    coupon_codes = {
    'BEACH2023':25,
    'ROMANCE2023':25,
    'FAMILYADVENT':25,
    'WINTER2023':25,
    'GOLFPARADISE':28,
    'SPARELAX':25,
    'FOODIE2023':18,
    'SKI2023':25,
    'BUSINESSPLUS':35,
    'TROPICS2023':25,
    'SUMMER2023':15,
    'FAMILYFUN':35
}   
    price=room_prices[room]
    if room in room_prices and coupon in coupon_codes:
        price = room_prices[room] - (room_prices[room]*coupon_codes[coupon]/100)

    return price
