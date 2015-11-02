# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20151102_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='url',
        ),
        migrations.AddField(
            model_name='user',
            name='receive_newsletter',
            field=models.BooleanField(default=True),
        ),
    ]
