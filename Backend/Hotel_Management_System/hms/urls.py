from django.contrib import admin
from django.urls import path
from hms import views

urlpatterns = [
    path('', views.Welcome, name='Welcome'),
    path('rooms', views.rooms, name='rooms'),
    path('blogs', views.blogs, name='blogs'),
    path('offers', views.offers, name='offers'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
]
