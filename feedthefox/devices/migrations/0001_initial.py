# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import feedthefox.devices.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('date', models.DateField(auto_now_add=True)),
                ('link', models.URLField(default=b'', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('model', models.CharField(max_length=120)),
                ('manufacturer', models.CharField(max_length=120)),
                ('image', models.ImageField(null=True, upload_to=feedthefox.devices.models._get_upload_file_name, blank=True)),
                ('comment', models.TextField(default=b'', blank=True)),
                ('builds', models.ManyToManyField(to='devices.Build', blank=True)),
            ],
            options={
                'ordering': ('manufacturer', 'model'),
            },
        ),
        migrations.CreateModel(
            name='DeviceInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imei', models.CharField(default=b'', max_length=17, blank=True)),
                ('device', models.ForeignKey(to='devices.Device')),
                ('user', models.ForeignKey(related_name='devices_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='device',
            name='users',
            field=models.ManyToManyField(related_name='devices', through='devices.DeviceInfo', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('manufacturer', 'model')]),
        ),
    ]
