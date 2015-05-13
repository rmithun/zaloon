# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_auto_20150512_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='signup_date',
        ),
        migrations.AlterField(
            model_name='plan',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 28, 11, 431080)),
        ),
        migrations.AlterField(
            model_name='plandetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 28, 11, 433010)),
        ),
        migrations.AlterField(
            model_name='useractivitieslist',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 28, 11, 432346)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 28, 11, 431651)),
        ),
    ]
