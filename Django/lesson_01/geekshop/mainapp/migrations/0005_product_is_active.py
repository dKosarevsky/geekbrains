# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-27 04:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_productcategory_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активна'),
        ),
    ]