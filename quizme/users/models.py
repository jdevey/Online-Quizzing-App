from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)
    macAddress = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.email
