# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0024_auto_20170410_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsys.Invoice'),
        ),
    ]
