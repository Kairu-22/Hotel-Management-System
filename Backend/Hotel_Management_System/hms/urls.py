from django.contrib import admin
from django.urls import path
from hms import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('rooms', views.rooms, name='rooms'),
    path('blogs', views.blogs, name='blogs'),
    path('offers', views.offers, name='offers'),

]
