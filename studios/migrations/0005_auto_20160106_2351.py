# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0004_auto_20160106_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 688459)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 671787)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 670719)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 672782), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 681743)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 673681)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 683619)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 689218)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 675225)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 684693)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 675974)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 687518)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 687602)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 682594)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 682692)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 690028)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 677814)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 680489)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 679531)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 6, 23, 51, 53, 674410)),
        ),
    ]
