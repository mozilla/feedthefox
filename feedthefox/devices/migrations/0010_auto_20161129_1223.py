# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0009_device_codename'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='codename',
            field=models.CharField(max_length=120, default='', blank=True),
        ),
    ]
