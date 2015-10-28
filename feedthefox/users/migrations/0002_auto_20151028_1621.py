# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.URLField(max_length=400, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=50, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ircname',
            field=models.CharField(max_length=50, default='', blank=True),
        ),
    ]
