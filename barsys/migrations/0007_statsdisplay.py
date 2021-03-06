# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 15:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0006_auto_20170404_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatsDisplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_by_number_of_purchases', models.BooleanField(default=True)),
                ('sort_by_total_cost', models.BooleanField(default=False)),
                ('show_by_default', models.BooleanField()),
                ('filter_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsys.Category')),
                ('filter_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='barsys.Product')),
            ],
        ),
    ]
