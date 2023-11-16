# vehicle/models.py
from django.db import models
from account.models import CustomUser  # Adjust the import based on your project structure

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
