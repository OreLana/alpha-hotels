from django.db import models
from django.utils import timezone
from authentication.models import User, Receptionist
from booking.models import Room

class PaymentType(models.Model):
    payment_type=models.CharField(default='paystack', max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.payment_type


class Payment(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Successful', 'Successful'),
        ('Failed','Failed')
    )
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    staff = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)



