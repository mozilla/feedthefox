# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20151110_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mozillian_username',
            field=models.CharField(max_length=254, blank=True, default=''),
        ),
    ]
