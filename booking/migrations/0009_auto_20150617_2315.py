# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0021_auto_20150617_2315'),
        ('booking', '0008_auto_20150612_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='MerchantDailyReportStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_date', models.DateField(default=datetime.date(2015, 6, 17))),
                ('report', models.FileField(upload_to=b'reports/%Y/%m/%d')),
                ('mail_sent', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 619730))),
                ('studio', models.ForeignKey(related_name=b'studio_report', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('promo_code', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='bookingdetails',
            old_name='apoointment_time',
            new_name='appointment_time',
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='booking_type',
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='is_valid',
            field=models.BooleanField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='promo',
            field=models.ForeignKey(related_name=b'applied_promo_code', to='booking.Promo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 615890)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 613359)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 616792)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 617535)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 617499)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 611680)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 6, 17, 23, 15, 49, 614798)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 614866)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 17, 23, 15, 49, 618756)),
        ),
    ]
