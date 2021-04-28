from django.contrib import admin
from .models.booking import Booking
from .models.payment import Payment, PaymentType


# Register your models here.
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(PaymentType)
