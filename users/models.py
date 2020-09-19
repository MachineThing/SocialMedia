from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as gettxt
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

from .managers import userMan

class SocialUser(AbstractUser, PermissionsMixin):
    email = models.EmailField(gettxt('email address'), unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='profile/', height_field=None, width_field=None)
    profile_bio = models.TextField(max_length=150, unique=False, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = userMan()

    def __str__(self):
        return self.username
