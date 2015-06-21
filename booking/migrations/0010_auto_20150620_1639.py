# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0009_auto_20150617_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyReminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_no', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=1)),
                ('message', models.TextField()),
                ('service_updated', models.CharField(max_length=30)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 331240))),
                ('booking', models.ForeignKey(related_name=b'dr_for_booking', to='booking.BookingDetails')),
                ('user', models.ForeignKey(related_name=b'dr_for_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HourlyReminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_no', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=1)),
                ('message', models.TextField()),
                ('service_updated', models.CharField(max_length=30)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 331802))),
                ('booking', models.ForeignKey(related_name=b'hr_reminder_for_booking', to='booking.BookingDetails')),
                ('user', models.ForeignKey(related_name=b'hr_for_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThanksMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_no', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=30)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 332349))),
                ('booking', models.ForeignKey(related_name=b'tm_for_booking', to='booking.BookingDetails')),
                ('user', models.ForeignKey(related_name=b'tm_for_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 328390)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 326876)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 328919)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 6, 20)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 330682)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 329375)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 329351)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 325897)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 6, 20, 16, 39, 42, 327735)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 327775)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 16, 39, 42, 330090)),
        ),
    ]
