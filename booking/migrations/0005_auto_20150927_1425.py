# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20150927_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 330789)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 327230)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 327299)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 331679)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 323993)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 326032)),
        ),
        migrations.AlterField(
            model_name='couponforusers',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 324926)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 338378)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 335585)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 336534)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 334613)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 332439)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 332399)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 322985)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 9, 27, 14, 25, 1, 329512)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 329582)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 339433)),
        ),
        migrations.AlterField(
            model_name='rzpayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 328582)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 333453)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 14, 25, 1, 337470)),
        ),
    ]
