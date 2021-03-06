# Generated by Django 3.2.2 on 2021-05-17 08:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20210514_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_users_chat',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 8, 32, 14, 893706, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='all_users_chat_message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 8, 32, 14, 894295, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 13, 2, 14, 891701)),
        ),
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 13, 2, 14, 893156)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 17, 13, 2, 14, 887988)),
        ),
    ]
