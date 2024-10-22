from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None):

        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def __str__(self):
        return self.email
