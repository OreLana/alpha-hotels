from django.db import models
from phone_field import PhoneField
from django.utils.translation import ugettext_lazy as _
from .user_manager import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_('email address'), max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    otp_code = models.CharField(max_length=50, unique=True, null=True)
    email_verfied = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username


class Receptionist(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=50)
    avatar_url = models.ImageField(upload_to='uploaded_avatars', null=True)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name
    
    
  
  

