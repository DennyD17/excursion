# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-17 21:11
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0004_auto_20161218_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(blank=True, editable=False, max_length=50),
        ),
    ]