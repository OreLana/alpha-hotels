from django.db import models
from django.utils import timezone
from authentication.models import User
from booking.models import Room
from .payment import Payment

# Create your models here.
class Booking(models.Model):
    room_no=models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    check_in=models.DateField(auto_now=False, auto_now_add=False)
    check_out=models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Booking ID: "+str(self.id)
        
    
