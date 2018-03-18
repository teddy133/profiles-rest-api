from django.db import models
from django.contrib.auth.models import BaseUserManager
# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(BaseUserManager):
    '''helps django work with the custumer user model'''
    def create_user(self, email, name, password=None):
        '''creates a new user Profile Object'''
        if not email:
            raise valueError('users Must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        '''creates and saves a new super user'''
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Respresents a users profile inside of our system'''
    email = models.EmailField(max_length=264, unique=True)
    name = models.CharField(max_length=264)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Use to get a user FUll name'''
        return self.name

    def get_short_name(self):
        '''used to get a users short name'''
        return self.name


    def __str__(self):
        return self.email
