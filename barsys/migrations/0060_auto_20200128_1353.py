# Generated by Django 2.1.11 on 2020-01-28 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barsys', '0059_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='Count',
            new_name='count',
        ),
    ]
