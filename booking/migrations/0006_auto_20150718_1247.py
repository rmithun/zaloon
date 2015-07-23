# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_auto_20150703_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_reviewed', models.BooleanField(default=0)),
                ('link_code', models.CharField(max_length=50)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 837362))),
                ('service_updated', models.CharField(max_length=30)),
                ('booking', models.ForeignKey(related_name=b'review_link_of_booking', to='booking.BookingDetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 828520)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 825944)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 829396)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 823818)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 824722)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 7, 18)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 836514)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 833329)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 834512)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 7, 18)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 832393)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 830201)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 830151)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 822866)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 7, 18, 12, 47, 20, 827443)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 827510)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 831221)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 18, 12, 47, 20, 835450)),
        ),
    ]
