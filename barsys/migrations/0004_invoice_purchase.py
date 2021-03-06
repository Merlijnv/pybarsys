# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 18:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0003_remove_category_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=40)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('product_amount', models.CharField(max_length=10)),
                ('quantity', models.PositiveIntegerField()),
                ('invoice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='barsys.Invoice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
