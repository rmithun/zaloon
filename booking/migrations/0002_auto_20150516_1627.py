# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 406160)),
        ),
        migrations.AlterField(
            model_name='activitytype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 405278)),
        ),
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 408323)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 407376)),
        ),
    ]
