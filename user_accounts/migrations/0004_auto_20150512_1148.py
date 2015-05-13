# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0003_auto_20150512_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='date_of_birth',
            new_name='dob',
        ),
        migrations.AlterField(
            model_name='plan',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 48, 20, 275787)),
        ),
        migrations.AlterField(
            model_name='plandetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 48, 20, 277648)),
        ),
        migrations.AlterField(
            model_name='useractivitieslist',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 48, 20, 276992)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 11, 48, 20, 276351)),
        ),
    ]
