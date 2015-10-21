import os
import uuid

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible


def _get_upload_file_name(instance, filename):
    return os.path.join(settings.USER_PHOTOS_DIR, str(uuid.uuid4()) + '.jpg')


@python_2_unicode_compatible
class Build(models.Model):
    """Model for FxOS builds."""

    name = models.CharField(max_length=120)
    date = models.DateField(auto_now_add=True)
    link = models.URLField(blank=True, default='')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Device(models.Model):
    """Model for FxOS devices."""

    model = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=120)
    imei = models.CharField(max_length=17, blank=True, default='')
    user = models.ForeignKey(User, related_name='devices',
                             blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=_get_upload_file_name, blank=True, null=True)
    comment = models.TextField(blank=True, default='')
    builds = models.ManyToManyField(Build, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.model, self.manufacturer)

    class Meta:
        ordering = ('manufacturer', 'model',)
        unique_together = ('manufacturer', 'model',)
