from django import forms
from django.contrib.auth import get_user_model
from .models import User
from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField()


    class Meta:
        model = User
        fields = ['username', 'email','phone_number', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField()