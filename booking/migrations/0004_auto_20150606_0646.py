# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20150606_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 6, 46, 45, 135171)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 6, 46, 45, 134522)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='user',
            field=models.ForeignKey(related_name=b'booked_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 6, 46, 45, 135701)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 6, 46, 45, 136318)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 6, 46, 45, 136297)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='customer',
            field=models.ForeignKey(related_name=b'user_who_purchased', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 6, 46, 45, 133880)),
        ),
    ]
