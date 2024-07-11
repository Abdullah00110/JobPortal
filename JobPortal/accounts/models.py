from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.

class UserManger(BaseUserManager):
    def create_user(self, email, name, tc, password = None, password2 = None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError(:)