# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0004_auto_20150512_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 41, 608811)),
        ),
        migrations.AlterField(
            model_name='plandetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 41, 612250)),
        ),
        migrations.AlterField(
            model_name='useractivitieslist',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 41, 611183)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 41, 609760)),
        ),
    ]
