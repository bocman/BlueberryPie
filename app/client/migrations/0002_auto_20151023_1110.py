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
            name='is_activated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='device_gpio',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
