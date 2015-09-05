# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0003_auto_20150902_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 123816)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 133323)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 127901)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 115000)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 114033)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 116245), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 128995)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 117291)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 124677)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 134133)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 135041)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='contact_no',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='primary_email',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 118964)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 131518)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 119752)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 132375)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 132457)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 130157)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 130234)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 135912)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='city',
            field=models.CharField(default=b'Chennai', max_length=40),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='contact_mobile_no',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='contact_person',
            field=models.CharField(max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='country',
            field=models.CharField(default=b'India', max_length=40),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='daily_studio_closed_from',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='daily_studio_closed_till',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='landline_no_1',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='landline_no_2',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='state',
            field=models.CharField(default=b'Tamil nadu', max_length=40),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 121792)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 125710)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 126968)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 2, 12, 11, 27, 118093)),
        ),
    ]
