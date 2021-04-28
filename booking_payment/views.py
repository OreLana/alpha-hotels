from django.shortcuts import render, redirect
from .forms import BookForm
from booking.models import Room
from .models.payment import Payment, PaymentType
from .models.booking import Booking
from authentication.models import Receptionist
from django.contrib import messages
import random
from datetime import datetime
from dateutil import parser
# Create your views here.
def book(request, pk):
    room = Room.objects.get(pk=pk)
    form = BookForm
    context = {
       "form":form,
       "room":room,
    }    
    return render(request, 'booking_payment/book.html', context)


def confirm_booking(request,pk):
    if request.method == 'POST':
        customer = request.user
        room = Room.objects.get(pk=pk)
        price = room.room_type.price
        checkin_date = parser.parse(request.POST.get('checkin')).date()
        checkout_date = parser.parse(request.POST.get('checkout')).date()
        if checkout_date > checkin_date:
            amount = price * (checkout_date - checkin_date).days
        elif checkout_date == checkin_date:
            amount = price
        else:
            messages.info(request, 'Checkout date must be greater than check in date')
            return redirect('book_room', pk=pk)

        receptionist = random.choice(Receptionist.objects.all())
        payment_type = PaymentType.objects.get(payment_type='paystack')

        create_payment = Payment.objects.create(status='pending', customer=customer, staff=receptionist, payment_type=payment_type)
        create_payment.save()

        create_booking = Booking.objects.create(room_no=room, customer=customer, check_in=checkin_date, check_out=checkout_date, payment=create_payment)
        create_booking.save()
        # booking = Booking.objects.get(customer=customer)
        context = {
            "room": room,
            "customer": customer,
            "checkin_date": checkin_date,
            "checkout_date": checkout_date,
            "amount":amount
        }
        return render(request, 'booking_payment/confirm_booking.html', context)

    