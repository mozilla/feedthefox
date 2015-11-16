# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20151111_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default='', max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(default='', max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='ircname',
            field=models.CharField(default='', max_length=63, blank=True),
        ),
    ]
