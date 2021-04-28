from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


class RoomType(models.Model):
    type = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.type


class RoomStatus(models.Model):
    STATUS = (
        ('Booked', 'Booked'),
        ('Available', 'Available'),
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.status)


class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
    room_number = models.IntegerField(null=False)
    description = models.TextField(null=True)
    created_at= models.DateTimeField(default=timezone.now)
    updated_at= models.DateTimeField(default=timezone.now)
    room_image=CloudinaryField('image', folder='hotelms')

    def __str__(self):
        return str(self.room_number)

