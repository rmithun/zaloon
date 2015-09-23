# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0022_auto_20150911_0227'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioinvoices',
            name='service_tax_amount',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 733636)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 724988)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 724343)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 725613), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 731210)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 726175)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 734115)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 727149)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='amount_to_be_paid',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='fee_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2015, 9, 22)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='service_updated',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='total_booking_amount',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 732377)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 727718)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 733000)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 733046)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 731740)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 731797)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 734638)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 728835)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 730582)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 729890)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 17, 36, 28, 726632)),
        ),
    ]
