from django.contrib import admin
from django.urls import path
from hms import views
from .views import user_logout
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

    path('booking_confirm/', views.booking_confirm, name='booking_confirm'),


    path('cleaning_manager', views.cleaning_manager, name='manager/cleaning'),
    path('checkout_room', views.checkout_room, name='checkout_room'),
    path('reception_manager', views.reception_manager, name='reception_manager'),
    path('book_room', views.book_room, name='book_room'),
    path('logout/', user_logout, name='logout'),
   
]
