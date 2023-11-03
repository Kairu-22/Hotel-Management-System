from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=255)
    current_status = models.CharField(max_length=255, choices=[
        ('Checked In', 'Checked In'),
        ('Checked Out & Clean', 'Checked Out & Clean'),
        ('Checked Out', 'Checked Out'),
    ])

    def __str__(self):
        return self.room_number


# Create your models here.
class Rooms_details(models.Model):
    room_type = models.CharField(max_length=35)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    number_of_rooms= models.IntegerField()
    def __str__(self):
        return self.room_type

class Bookings(models.Model):
    booking_ID=models.CharField(max_length=15)
    Username=models.CharField(max_length=15)
    checkin=models.DateField()
    checkout=models.DateField()
    room_type = models.CharField(max_length=35)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    guest_count=models.IntegerField()
    def __str__(self):
        return self.booking_ID

    
class Offers(models.Model):
    offer = models.CharField(max_length=20)
    percentage = models.DecimalField(decimal_places=2, max_digits=4)
    room_type = models.CharField(max_length=35)
    def __str__(self):
        return self.offer

