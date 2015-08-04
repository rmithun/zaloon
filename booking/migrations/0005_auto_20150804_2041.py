# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20150802_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='RZPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rzp_payment_id', models.CharField(max_length=100)),
                ('rzp_status', models.CharField(max_length=30)),
                ('service_updated', models.CharField(max_length=25)),
                ('refund_id', models.CharField(max_length=100, null=True)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 51655))),
                ('purchase', models.ForeignKey(related_name=b'purchase_id_rzp', to='booking.Purchase')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 52976)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 50703)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 53527)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 49376)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 49943)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 8, 4)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 59785)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 57876)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 58484)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 8, 4)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 57287)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 55990)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 55946)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 48791)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 8, 4, 20, 41, 57, 52224)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 52264)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 60300)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 56679)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 4, 20, 41, 57, 59225)),
        ),
    ]
