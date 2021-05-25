from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from profiles_api.model.m_user_profile_manager import UserProfileManager


# first load class in the project
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""  # python docs

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name user"""
        return self.name

    def get_short_name(self):
        """Retrieve short name user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
