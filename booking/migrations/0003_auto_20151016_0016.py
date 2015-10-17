# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '__first__'),
        ('booking', '0002_auto_20151016_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyInvoiceConfirmation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_for_date', models.DateField(default=datetime.date(2015, 10, 15))),
                ('booking_pdf', models.FileField(upload_to=b'invoices/%Y/%m/%d')),
                ('mail_sent', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=50)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 586785))),
                ('studio', models.ForeignKey(related_name=b'studio_invoices', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 578182)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='booking_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 572664)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 572733)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 579052)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 569314)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 571438)),
        ),
        migrations.AlterField(
            model_name='couponforusers',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 570508)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 585883)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 582916)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 583847)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 581994)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 579790)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 579754)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 568268)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 10, 16, 0, 16, 38, 577062)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 577137)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 587604)),
        ),
        migrations.AlterField(
            model_name='rzpayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 574007)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 580835)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 16, 38, 584810)),
        ),
    ]
