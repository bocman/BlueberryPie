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
                ('name', models.CharField(default=b'Not set yet', max_length=30)),
                ('description', models.CharField(default=b'Not set yet', max_length=30)),
                ('is_general', models.BooleanField(default=False)),
                ('pin_number', models.PositiveIntegerField(default=None, null=True)),
                ('interval', models.PositiveIntegerField(default=0, null=True, verbose_name=b'Time interval')),
                ('is_input', models.NullBooleanField(default=False)),
                ('client', models.PositiveIntegerField(default=None)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'GPIO',
            },
        ),
    ]
