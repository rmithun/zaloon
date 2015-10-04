# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150908_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetails',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 899407)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='purchase',
            name='service_tax',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 903158)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 899450)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 903769)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 897338)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 898657)),
        ),
        migrations.AlterField(
            model_name='couponforusers',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 897942)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 9, 16)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='service_updated',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 907998)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 906252)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 906840)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 9, 16)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 905539)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 904246)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 904223)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 896706)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 9, 16, 23, 51, 1, 900820)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 900863)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 908510)),
        ),
        migrations.AlterField(
            model_name='rzpayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 900234)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 904883)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 23, 51, 1, 907418)),
        ),
    ]
