# Generated by Django 3.2.9 on 2021-11-07 11:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='likes',
        ),
        migrations.AlterField(
            model_name='comment',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 16, 46, 37, 43346)),
        ),
    ]
