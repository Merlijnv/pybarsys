# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0028_productchangeaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productchangeaction',
            name='products',
            field=models.ManyToManyField(help_text='Only these products will be changed.', to='barsys.Product'),
        ),
    ]