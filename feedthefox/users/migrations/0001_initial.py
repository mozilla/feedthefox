# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ircname', models.CharField(default=b'', max_length=50, blank=True)),
                ('avatar_url', models.URLField(default=b'', max_length=400, blank=True)),
                ('city', models.CharField(default=b'', max_length=50, blank=True)),
                ('country', models.CharField(default=b'', max_length=50, blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
