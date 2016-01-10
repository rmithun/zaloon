# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0005_auto_20160106_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 340000)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 325348)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 324251)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 326243), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 335220)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 327213)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2016, 1, 10)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 337118)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 340766)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 328756)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2016, 1, 10)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 338284)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 329677)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 339146)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 339219)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 336097)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 336186)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 341557)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 331262)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 334116)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 333001)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 10, 12, 11, 13, 327949)),
        ),
    ]
