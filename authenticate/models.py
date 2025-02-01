from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, name, email, password=None):

        if email is None:
            raise TypeError('Users should have an Email')
        if password is None:
            raise TypeError('password can not be none')

        user = self.model(name=name, email=self.normalize_email(email))
        user.set_password(password) #hash password
        '''
        When using multiple databases in a Django project, 
        self._db specifies in which database the current object will be stored.
        If we remove using=self._db, by default, 
        Django will only use the main database (default) and problems may occur when using multiple databases.
        '''
        user.save(using=self._db) 
        return user

    def create_superuser(self, name, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db) 
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


    # def save(self, *args, **kwargs):
    #     '''
    #     hash password just in admin pannel
    #     '''
    #     '''
    #     When you override the model's save method, 
    #     you must pass *args, **kwargs to preserve all of the default save() arguments.
    #     '''
    #     if self._state.adding or not self.password.startswith('pbkdf2_sha256$'):
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)    