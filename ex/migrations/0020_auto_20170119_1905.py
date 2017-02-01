# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ex', '0019_excursionimagestorage_img_alt'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogImageStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images', verbose_name='Изображение')),
                ('img_alt', models.CharField(blank=True, max_length=100, verbose_name='Описание изображения (опционально')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ex.Blog')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения для Блога',
            },
        ),
        migrations.AlterModelOptions(
            name='excursionimagestorage',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения для экскурсий'},
        ),
    ]