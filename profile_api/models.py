from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def Create_User(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an user address")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password["password"]
        user.save(using=self._db)
        return User

    def create_superuser(self,email,name,password):
        """create and save a new superuser with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return User





class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in the system"""
    email=models.EmailField(max_length=250,unique=True)
    name=models.CharField(max_length=250)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["name"]

    def get_full_name(self):
        """retrieve full name user"""
        return self.name

    def get_short_name(self):
        """retrive short name of user"""
        return self.name

    def __str__(self):
        """return string representation of our user"""
        return self.email
