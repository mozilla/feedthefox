# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import feedthefox.devices.models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0005_auto_20151105_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinfo',
            name='imei',
            field=models.CharField(default='', blank=True, max_length=17, validators=[feedthefox.devices.models.validate_imei]),
        ),
    ]
