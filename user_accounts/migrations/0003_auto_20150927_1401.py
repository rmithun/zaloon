# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0002_auto_20150920_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationusers',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 1, 9, 718947)),
        ),
        migrations.AlterField(
            model_name='userinvites',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 1, 9, 718273)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 1, 9, 717430)),
        ),
    ]
