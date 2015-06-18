# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0010_auto_20150614_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvites',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 41, 373150)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 41, 372113)),
        ),
    ]
