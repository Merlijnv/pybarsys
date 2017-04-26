# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0045_auto_20170426_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freeitem',
            name='purchasable',
            field=models.BooleanField(default=True, help_text='Whether these free items are shown on the main purchase page. If no, only admins can change the leftover quantity.'),
        ),
    ]
