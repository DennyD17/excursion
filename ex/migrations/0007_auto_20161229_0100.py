# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-29 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0006_auto_20161229_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='event_date',
            field=models.DateField(),
        ),
    ]
