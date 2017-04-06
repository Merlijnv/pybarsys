# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0012_auto_20170406_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('name', 'amount')]),
        ),
    ]