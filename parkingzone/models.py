from django.db import models

# Create your models here.

class Slot(models.Model):
    time_duration = models.IntegerField()
    cost = models.FloatField()
