# Generated by Django 2.2.24 on 2021-08-23 15:42

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181227_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='featured_image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, upload_to='blog', verbose_name='Featured Image'),
        ),
    ]
