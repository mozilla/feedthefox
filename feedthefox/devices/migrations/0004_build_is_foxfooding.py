# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_device_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='is_foxfooding',
            field=models.BooleanField(default=False),
        ),
    ]
