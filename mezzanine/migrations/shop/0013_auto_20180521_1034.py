# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-05-21 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20180313_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_detail_state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State/Region'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_detail_state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State/Region'),
        ),
    ]
