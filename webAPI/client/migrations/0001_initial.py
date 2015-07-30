# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device_GPIO',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pin_number', models.PositiveSmallIntegerField(default=None, null=True, blank=True)),
                ('is_activated', models.BooleanField(default=False)),
                ('is_input', models.NullBooleanField(default=False)),
                ('interval', models.PositiveIntegerField(default=0, null=True)),
                ('is_general', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'GPIO',
            },
        ),
    ]
