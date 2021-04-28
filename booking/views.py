from django.shortcuts import render
from .models import Room

# Create your views here.
def about(request):
    return render(request, "booking/about.html", context=None)


def rooms(request):
    all_rooms = Room.objects.all()
    context = {
        "all_rooms": all_rooms,
    }
    return render(request, "booking/rooms.html", context)

def room_detail(request, pk):
    room = Room.objects.get(pk=pk)
    context = {
        "room": room,
    }

    return render(request, "booking/room_detail.html", context)

