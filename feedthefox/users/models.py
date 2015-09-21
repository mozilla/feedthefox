from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class UserProfile(models.Model):
    """Basic Mozillian user profile."""

    user = models.OneToOneField(User, related_name='profile')
    ircname = models.CharField(max_length=50, default='', blank=True)
    avatar_url = models.URLField(max_length=400, default='', blank=True)
    city = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.user.get_full_name()
