# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-12 21:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name_plural': 'Product Categories'},
        ),
    ]
