# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0008_auto_20170405_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='statsdisplay',
            name='title',
            field=models.CharField(default='Testtitel', max_length=30),
            preserve_default=False,
        ),
    ]
