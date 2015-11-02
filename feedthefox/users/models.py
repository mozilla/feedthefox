from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    """Basic Mozillian user profile."""

    ircname = models.CharField(max_length=50, default='', blank=True)
    photo = models.URLField(max_length=400, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    receive_newsletter = models.BooleanField(default=True)

    def __str__(self):
        return self.get_full_name()
