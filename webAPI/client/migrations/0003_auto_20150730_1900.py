# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20150729_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_gpio',
            name='client',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
