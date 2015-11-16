import base64
import hashlib

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
try:
    from django.utils.encoding import smart_bytes
except ImportError:
    from django.utils.encoding import smart_str as smart_bytes


@python_2_unicode_compatible
class User(AbstractUser):
    """Basic Mozillian user profile."""

    ircname = models.CharField(max_length=63, default='', blank=True)
    photo = models.URLField(max_length=400, default='', blank=True)
    city = models.CharField(max_length=120, default='', blank=True)
    country = models.CharField(max_length=120, default='', blank=True)
    receive_newsletter = models.BooleanField(default=True)
    foxfooding_interest = models.BooleanField(default=False)
    mozillian_username = models.CharField(max_length=254, default='', blank=True)

    def __str__(self):
        return self.get_full_name()

    class Meta(object):
        unique_together = ('email',)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.username = base64.urlsafe_b64encode(hashlib.sha1(
                smart_bytes(self.email)).digest()
            ).rstrip(b'=')
        super(User, self).save()
