# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0006_auto_20151001_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='min_booking_amount',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 716361)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 712200)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 712244)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 716899)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='discount_value',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 710183)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 711474)),
        ),
        migrations.AlterField(
            model_name='couponforusers',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 710916)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 10, 8)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 721449)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 719616)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 720213)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 10, 8)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 718946)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 717448)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 717425)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 709468)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 10, 8, 16, 41, 51, 715456)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 715503)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 722265)),
        ),
        migrations.AlterField(
            model_name='rzpayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 713066)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 718078)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 8, 16, 41, 51, 720893)),
        ),
    ]
