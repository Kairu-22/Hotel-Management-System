from django.contrib import admin
from django.urls import path
from hms import views

urlpatterns = [
    path('', views.Welcome, name='Welcome'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('rooms', views.rooms, name='rooms'),
    path('booking', views.booking, name='booking'),
    path('blogs', views.blogs, name='blogs'),
    path('offers', views.offers, name='offers'),
    path('gallery', views.gallery, name='gallery'),
    path('booking_verification', views.booking_verification, name='booking_verification'),
    path('dashboard', views.dashboard, name='dashboard'),  
    path('booking_confirm/', views.booking_confirm, name='booking_confirm'),
]
