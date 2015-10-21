# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
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
                ('imei', models.CharField(default=b'', max_length=17, blank=True)),
                ('image', models.ImageField(null=True, upload_to=feedthefox.devices.models._get_upload_file_name, blank=True)),
                ('comment', models.TextField(default=b'', blank=True)),
                ('builds', models.ManyToManyField(to='devices.Build', blank=True)),
                ('user', models.ForeignKey(related_name='devices', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('manufacturer', 'model'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='device',
            unique_together=set([('manufacturer', 'model')]),
        ),
    ]
