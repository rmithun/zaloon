# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0002_auto_20150723_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioprofile',
            name='closing_at',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='daily_studio_closed_from',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='daily_studio_closed_till',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='opening_at',
            field=models.TimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 723169)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 728414)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 725476)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 718472)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 717928)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 719000), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 726059)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 719646)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 723711)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 729117)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 729660)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 720678)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 727299)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 721253)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 727789)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 727833)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 726675)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 726718)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 730180)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 722267)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 724271)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 724851)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 16, 54, 720074)),
        ),
    ]
