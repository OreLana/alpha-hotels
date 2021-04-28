from django.urls import path, include
from . import views

urlpatterns = [
    path("about/",views.about, name="about"),
    path("rooms/", views.rooms, name="rooms"),
    path("<int:pk>/", views.room_detail, name="room_detail"),
    path("<int:pk>/book/", include('booking_payment.urls')),
]