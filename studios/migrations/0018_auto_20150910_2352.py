# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0017_auto_20150908_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studioamenities',
            name='amenity',
        ),
        migrations.DeleteModel(
            name='Amenities',
        ),
        migrations.RemoveField(
            model_name='studioamenities',
            name='studio_profile',
        ),
        migrations.DeleteModel(
            name='StudioAmenities',
        ),
        migrations.RemoveField(
            model_name='studioclosedfromtill',
            name='studio',
        ),
        migrations.DeleteModel(
            name='StudioClosedFromTill',
        ),
        migrations.RemoveField(
            model_name='studiostaffcounts',
            name='studio_profile',
        ),
        migrations.DeleteModel(
            name='StudioStaffCounts',
        ),
        migrations.RenameField(
            model_name='studioinvoices',
            old_name='last_payment_amount',
            new_name='fee_amount',
        ),
        migrations.RemoveField(
            model_name='studioaccountdetails',
            name='mode_of_payment',
        ),
        migrations.RemoveField(
            model_name='studioinvoices',
            name='last_payment_date',
        ),
        migrations.RemoveField(
            model_name='studioinvoices',
            name='payment_requested',
        ),
        migrations.RemoveField(
            model_name='studiopayment',
            name='mode_of_payment',
        ),
        migrations.DeleteModel(
            name='PaymentModes',
        ),
        migrations.AddField(
            model_name='studioinvoices',
            name='total_booking',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studioinvoices',
            name='total_booking_amount',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studiopayment',
            name='disputed',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 265069)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 251438)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 250551)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 252636), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 261533)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 253566)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 267667)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 255087)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 263424)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 255817)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 264183)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 264256)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 262444)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 262539)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 268794)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 257620)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 260264)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 259318)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 10, 23, 52, 30, 254288)),
        ),
    ]
