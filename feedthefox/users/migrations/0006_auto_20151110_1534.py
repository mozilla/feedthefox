# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_foxfooding_interest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='mozillian_username',
            field=models.CharField(default=b'', max_length=254, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([('email',)]),
        ),
    ]
