# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imei', models.CharField(default=b'', max_length=17, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='device',
            name='imei',
        ),
        migrations.RemoveField(
            model_name='device',
            name='user',
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='device',
            field=models.ForeignKey(to='devices.Device'),
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='user',
            field=models.ForeignKey(related_name='devices_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='device',
            name='users',
            field=models.ManyToManyField(related_name='devices', through='devices.DeviceInfo', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
