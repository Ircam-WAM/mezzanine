# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-05-22 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20180522_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_detail_phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
    ]
