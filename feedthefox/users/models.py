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
    foxfooding_interest = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name()

    class Meta(object):
        unique_together = ('email',)

    def save(self, *args, **kwargs):
        if not self.pk and User.objects.filter(username=self.username).exists():
            self.username = u'{0} - {1}'.format(self.username, self.email)
        super(User, self).save()
