# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150516_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 28, 2, 943263)),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 28, 2, 942366)),
        ),
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 28, 2, 945381)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 28, 2, 944437)),
        ),
    ]
