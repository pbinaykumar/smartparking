# account/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     list_display = ('id', 'email', 'name', 'is_active', 'is_staff')
#     search_fields = ('email', 'name')
#     ordering = ('email',)
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('name',)}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#     )

admin.site.register(CustomUser)
