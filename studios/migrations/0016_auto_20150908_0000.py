# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0015_auto_20150907_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 485729)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 496906)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 490257)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 478010)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 477109)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 479136), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 491222)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 480055)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 486496)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 497737)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 498589)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 481604)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 495315)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 482339)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 496083)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 496155)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 492231)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 494240)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 499748)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 484062)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 488462)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 487343)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 489435)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 0, 27, 480778)),
        ),
    ]
