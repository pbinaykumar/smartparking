from django.contrib import admin

# Register your models here.

# vehicle/admin.py
from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'user')
    list_filter = ('user',)
