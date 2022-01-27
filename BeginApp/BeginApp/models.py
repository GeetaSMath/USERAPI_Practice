from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField('username')
    email = models.EmailField(('email address'),unique=True)
    password = models.IntegerField('password')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email