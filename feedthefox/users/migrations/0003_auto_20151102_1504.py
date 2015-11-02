# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151028_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatar_url',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mozillians_url',
        ),
        migrations.AddField(
            model_name='user',
            name='url',
            field=models.URLField(default=b'', max_length=150, blank=True),
        ),
    ]
