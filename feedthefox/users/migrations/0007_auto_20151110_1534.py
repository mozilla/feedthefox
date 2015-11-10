# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def forwards(apps, schema_editor):
    """Populate mozillian_username with username data."""
    User = apps.get_model('users', 'User')
    users = User.objects.all()
    for user in users:
        user.mozillian_username = user.username
        user.save()


def backwards(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20151110_1534'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards)
    ]
