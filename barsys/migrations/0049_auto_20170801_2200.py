# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-01 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0048_auto_20170801_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='product_amount',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_category',
            field=models.CharField(max_length=40),
        ),
    ]