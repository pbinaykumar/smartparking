import imp
from pyexpat import model
from django.db import models
import uuid
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)
import uuid
from django.conf import settings


class UserManager(BaseUserManager):
    def create_user(self, is_admin=False, is_active=False, is_staff=False, password=False, *args, **kwargs):

        user = self.model(
            email=self.normalize_email(kwargs.get('email'))
        )

        for field in ['email','name']:
            if not kwargs.get(field):
                raise ValueError(f"Users must have an {field}")
        user.name = kwargs.get("name")
        user.set_password(password)
        user.admin = is_admin
        user.active = True
        user.staff = is_staff

        user.save(using=self._db)

        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(
            is_admin=True,
            is_staff=True,
            is_active=True,
            *args,
            **kwargs,
        )
        return user


class User(AbstractBaseUser):

    user_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, )
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    # lastName = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)


    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return str(self.email)

    def get_user_email(self):
        return str(self.email)

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
