# vehicle/models.py
from django.db import models
from account.models import User  # Adjust the import based on your project structure

class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=20,unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Slot(models.Model):
    time_duration = models.IntegerField()
    cost = models.FloatField()
class History(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    in_time = models.DateTimeField(auto_now_add=True)
    out_time = models.DateTimeField()
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    slot_cost = models.FloatField()
    extra_cost = models.FloatField()
    total_cost = models.FloatField()

