from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(AbstractUser):
    """Basic Mozillian user profile."""

    ircname = models.CharField(max_length=50, default='', blank=True)
    avatar_url = models.URLField(max_length=400, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    mozillians_url = models.URLField()

    def __str__(self):
        return self.user.get_full_name()
