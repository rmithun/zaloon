# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20150802_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 790125)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='is_reviewed',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 788700)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 790649)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 787332)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 787855)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 796484)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 794668)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 795272)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 794098)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 791177)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 791155)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 786750)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 8, 2, 15, 56, 11, 789480)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 789518)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 796985)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 793416)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 15, 56, 11, 795940)),
        ),
    ]
