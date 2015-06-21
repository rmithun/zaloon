# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20150620_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thanksmail',
            name='mobile_no',
        ),
        migrations.AddField(
            model_name='thanksmail',
            name='email',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='email',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 46663)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 45090)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 47217)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 49570)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 50170)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 48998)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 47682)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 47659)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 44090)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 6, 20, 23, 32, 52, 45972)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 46013)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 48398)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 23, 32, 52, 50731)),
        ),
    ]
