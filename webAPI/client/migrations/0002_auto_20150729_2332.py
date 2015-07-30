# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device_gpio',
            name='client',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='device_gpio',
            name='description',
            field=models.CharField(default=b'Not set yet', max_length=30),
        ),
        migrations.AddField(
            model_name='device_gpio',
            name='group',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AddField(
            model_name='device_gpio',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='device_gpio',
            name='name',
            field=models.CharField(default=b'Not set yet', max_length=30),
        ),
        migrations.AlterField(
            model_name='device_gpio',
            name='interval',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name=b'Time interval'),
        ),
        migrations.AlterField(
            model_name='device_gpio',
            name='pin_number',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
