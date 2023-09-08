# Generated by Django 3.2.19 on 2023-06-22 11:10

from django.db import migrations
import mezzanine.pages.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_merge_20230424_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='in_menus',
            field=mezzanine.pages.fields.MenusField(blank=True, choices=[(1, 'Header'), (2, 'Footer'), (3, 'Participate')], max_length=100, null=True, verbose_name='Show in menus'),
        ),
    ]