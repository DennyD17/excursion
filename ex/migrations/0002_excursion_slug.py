# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='slug',
            field=models.SlugField(default='dw', unique=True, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]
