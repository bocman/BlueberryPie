# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorTemperatureHumidity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.PositiveIntegerField(default=None, null=True)),
                ('humidity', models.PositiveSmallIntegerField(default=None, null=True)),
                ('gpio_id', models.PositiveIntegerField(default=None, null=True)),
                ('timestamp', models.DateTimeField(editable=False)),
            ],
            options={
                'db_table': 'data_temperature_humidity',
            },
        ),
    ]
