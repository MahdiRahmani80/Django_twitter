# Generated by Django 3.2.2 on 2021-05-08 13:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_users_chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 18, 1, 21, 56711)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 18, 1, 21, 54823)),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 18, 1, 21, 56143)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 8, 18, 1, 21, 51334)),
        ),
    ]