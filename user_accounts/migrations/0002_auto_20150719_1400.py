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
            model_name='userinvites',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 14, 0, 31, 686001)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 19, 14, 0, 31, 685167)),
        ),
    ]
