from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import User

class UserAdmin(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('user_id', 'email', 'admin', 'active')
    list_filter = ('admin', 'staff', 'admin')
    fieldsets = (
        ('Personal info', {'fields': ('name','email', 'password')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'firstName', 'lastName', 'password1', 'password2')}
    #      ),
    # )
    # search_fields = ('email', 'firstName', 'lastName')
    ordering = ('user_id',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)