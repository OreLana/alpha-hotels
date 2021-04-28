from .base import *
from decouple import config

DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hoteldb',
        'USER': config('USER'),
        'PASSWORD': config('PASSWORD'),
    }
}

