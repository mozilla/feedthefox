# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0006_auto_20151110_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='is_foxfooding',
            field=models.BooleanField(default=False),
        ),
    ]
