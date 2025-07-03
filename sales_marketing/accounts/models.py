from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('salesman', 'Salesman'),
        ('marketing', 'Marketing'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='salesman')

    def __str__(self):
        return self.username
