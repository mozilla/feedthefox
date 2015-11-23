# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_auto_20151112_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='codename',
            field=models.CharField(default=b'', max_length=120, blank=True),
        ),
    ]
