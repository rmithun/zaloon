# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0009_auto_20150802_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioaccountdetails',
            name='transaction_percent',
            field=models.PositiveIntegerField(default=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 616493)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 622121)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 618905)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 610109)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 609233)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 611227), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 619547)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 612150)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 617017)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 622633)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 623186)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 613709)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 621027)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 614462)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 621550)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 621598)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 620212)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 620257)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 623875)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='closing_at',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='opening_at',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 615479)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 617759)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 618365)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 13, 11, 51, 49, 612890)),
        ),
    ]
