# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-31 13:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0008_auto_20161231_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplereg',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ex.Excursion', verbose_name='Экскурсия'),
        ),
    ]
