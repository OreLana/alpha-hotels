from django.contrib import admin
from .models import User, Receptionist

# Register your models here.
@admin.register(User)
class MyModelAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.password)
        obj.save()
# admin.site.register(User)
admin.site.register(Receptionist)