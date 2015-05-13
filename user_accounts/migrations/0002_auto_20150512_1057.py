# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 53, 148733)),
        ),
        migrations.AlterField(
            model_name='plandetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 53, 150689)),
        ),
        migrations.AlterField(
            model_name='useractivitieslist',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 53, 150045)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_login',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 53, 149324)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 53, 149305)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 53, 149356)),
        ),
    ]
