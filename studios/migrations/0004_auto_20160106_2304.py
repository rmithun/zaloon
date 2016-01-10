# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0003_auto_20151016_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioaccountdetails',
            name='name',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studioservices',
            name='service_for',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 130732)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 113014)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 111655)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 114169), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 123490)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 115204)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2016, 1, 6)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 125842)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 131518)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 117004)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2016, 1, 6)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 126963)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 117741)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 129807)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 129893)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 124543)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 124652)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 132374)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 119496)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 122189)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 121245)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 4, 43, 116103)),
        ),
    ]
