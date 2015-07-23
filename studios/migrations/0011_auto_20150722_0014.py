# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0010_auto_20150722_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 109031)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 119217)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 114379)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 101097)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 100242)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 102227), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='studio',
            field=models.OneToOneField(related_name=b'studio_account_detail', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 115359)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 103145)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 109807)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='studio',
            field=models.OneToOneField(related_name=b'studio_closed_details', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 120006)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='studio',
            field=models.OneToOneField(related_name=b'studio_long_closed_details', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 120891)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 104882)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 117568)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 105759)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 118382)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 118453)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 116376)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 116442)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 121918)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 107512)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 112463)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='studio_profile',
            field=models.OneToOneField(related_name=b'studio_staff_count', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 113515)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 22, 0, 13, 59, 103886)),
        ),
    ]
