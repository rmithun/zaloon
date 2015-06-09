# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0015_auto_20150606_0741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studioprofile',
            old_name='is_not_closed',
            new_name='is_closed',
        ),
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 992945)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 998042)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 995122)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 989386)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 988881)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 989915), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_account_detail', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 995695)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'studio_amenities', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 993420)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_closed_details', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 998505)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_long_closed_details', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 999023)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 991011)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_invoice_detail', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 997036)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 997507)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 997546)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 996315)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_payment_detail', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 996354)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'pic_of_studio', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 999634)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 992077)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'studio_detail_for_activity', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 994072)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'studio_staff_count', to='studios.StudioProfile'),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 994632)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 8, 2, 29, 990410)),
        ),
    ]
