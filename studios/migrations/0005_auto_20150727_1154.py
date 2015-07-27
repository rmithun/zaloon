# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0004_auto_20150726_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 192689)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 197940)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 194960)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 187793)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 187279)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 188471), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 195580)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 189036)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 193186)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 198520)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 199060)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 190156)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 196922)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 190696)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 197404)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 197448)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 196176)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 196220)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 199723)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 191778)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 193885)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 194450)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 27, 11, 54, 58, 189489)),
        ),
    ]
