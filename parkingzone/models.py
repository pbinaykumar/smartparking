from django.db import models

# Create your models here.

class Slot(models.Model):
    time_duration = models.IntegerField()
    cost = models.FloatField()

class Zone(models.Model):
    name = models.CharField(max_length=101)
    qr_id = models.CharField(max_length=201,unique=True)

    def __str__(self):
        return self.name
