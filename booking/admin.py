from django.contrib import admin
from .models import RoomType,RoomStatus,Room


# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(RoomStatus)
