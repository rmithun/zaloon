# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150802_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 670081)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='is_reviewed',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 668641)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 670604)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 667281)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 667811)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 676440)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 674554)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 675201)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 673982)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 671093)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 671070)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 666673)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 8, 2, 11, 57, 7, 669419)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 669457)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 676945)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 673302)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 11, 57, 7, 675873)),
        ),
    ]
