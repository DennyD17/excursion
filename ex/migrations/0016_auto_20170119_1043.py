# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 10:43
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0015_auto_20170119_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplereg',
            name='date',
            field=models.DateTimeField(verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='event_date',
            field=models.DateField(verbose_name='Дата посещения'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='excursion',
            field=models.CharField(max_length=50, verbose_name='Экскурсия'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Отзыв'),
        ),
    ]