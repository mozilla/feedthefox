# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_auto_20151022_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='link',
            field=models.URLField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='comment',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AlterField(
            model_name='deviceinfo',
            name='imei',
            field=models.CharField(default='', max_length=17, blank=True),
        ),
    ]
