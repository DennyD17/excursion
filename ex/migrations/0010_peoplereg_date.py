# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 14:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0009_auto_20161231_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='peoplereg',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 31, 14, 23, 31, 288316), verbose_name='Дата и время'),
            preserve_default=False,
        ),
    ]
