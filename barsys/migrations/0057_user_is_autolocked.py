# Generated by Django 2.0.3 on 2018-10-03 19:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('barsys', '0056_auto_20180309_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_autolocked',
            field=models.BooleanField(default=False,
                                      help_text='User was automatically lockeddue to the outstanding balance'),
        ),
    ]