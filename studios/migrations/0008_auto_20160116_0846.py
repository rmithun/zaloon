# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0007_auto_20160110_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 467819)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 453113)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 451936)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 454048), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 463053)),
        ),
        migrations.AlterField(
            model_name='studioaddrequest',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 454996)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2016, 1, 16)),
        ),
        migrations.AlterField(
            model_name='studiobookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 464949)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 468594)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 456530)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='invoice_date',
            field=models.DateField(default=datetime.date(2016, 1, 16)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 466145)),
        ),
        migrations.AlterField(
            model_name='studiokind',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 457487)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 466979)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 467062)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 463903)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 464003)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 469457)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='has_service_tax',
            field=models.FloatField(default=14),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 459070)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 462021)),
        ),
        migrations.AlterField(
            model_name='studioservicetypes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 460854)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 16, 8, 46, 9, 455724)),
        ),
    ]
