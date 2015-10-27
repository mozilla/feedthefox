# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar_url',
            field=models.URLField(default='', max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(default='', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(default='', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ircname',
            field=models.CharField(default='', max_length=50, blank=True),
        ),
    ]
