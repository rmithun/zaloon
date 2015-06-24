# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0015_auto_20150621_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvites',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 23, 41, 21, 338086)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 23, 23, 41, 21, 337028)),
        ),
    ]
