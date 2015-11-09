# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0004_build_is_foxfooding'),
    ]

    operations = [
        migrations.AddField(
            model_name='build',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='device',
            name='link',
            field=models.URLField(blank=True, default=''),
        ),
    ]
