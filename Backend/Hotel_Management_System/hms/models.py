from django.db import models



# Create your models here.
class Rooms_details(models.Model):
    room_type = models.CharField(max_length=35)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    number_of_rooms= models.IntegerField()
    def __str__(self):
        return self.room_type

class Bookings(models.Model):
    booking_ID=models.IntegerField()
    Username=models.CharField(max_length=15)
    checkin=models.DateField()
    checkout=models.DateField()
    room_type = models.CharField(max_length=35)
    total_price = models.DecimalField(decimal_places=2, max_digits=8)
    guest_count=models.IntegerField()
    def __str__(self):
        return self.booking_ID