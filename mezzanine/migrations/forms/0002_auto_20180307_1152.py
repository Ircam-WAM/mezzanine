# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-03-07 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='help_text',
            field=models.TextField(blank=True, verbose_name='Help text'),
        ),
        migrations.AlterField(
            model_name='field',
            name='help_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Help text'),
        ),
        migrations.AlterField(
            model_name='field',
            name='help_text_fr',
            field=models.TextField(blank=True, null=True, verbose_name='Help text'),
        ),
        migrations.AlterField(
            model_name='field',
            name='label',
            field=models.TextField(verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='field',
            name='label_en',
            field=models.TextField(null=True, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='field',
            name='label_fr',
            field=models.TextField(null=True, verbose_name='Label'),
        ),
    ]