from django.urls import path
from . import views

urlpatterns = [
    path("", views.book, name="book_room"),
    path("confirm", views.confirm_booking, name="confirm_booking"),
]