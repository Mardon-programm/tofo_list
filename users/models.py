from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    age = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.username