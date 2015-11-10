# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20151102_1555'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='foxfooding_interest',
            field=models.BooleanField(default=False),
        ),
    ]
