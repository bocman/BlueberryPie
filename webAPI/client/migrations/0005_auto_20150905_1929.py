# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20150730_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device_gpio',
            name='group',
        ),
        migrations.AddField(
            model_name='device_gpio',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
