# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0002_auto_20150604_1721'),
        ('user_accounts', '0002_auto_20150604_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedMessageSend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('is_successful', models.BooleanField(default=0)),
                ('type_of_message', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=25)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 17, 21, 57, 81729))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booked_date', models.DateTimeField()),
                ('appointment_date', models.DateField()),
                ('apoointment_time', models.FloatField()),
                ('booking_code', models.CharField(max_length=25)),
                ('booking_status', models.CharField(max_length=30)),
                ('reminder_sent', models.BooleanField(default=0)),
                ('booking_type', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 17, 21, 57, 81065))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 17, 21, 57, 82263))),
                ('booking', models.ForeignKey(related_name=b'service_booked_with', to='booking.BookingDetails')),
                ('service', models.ForeignKey(related_name=b'service_booked', to='studios.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_paid', models.FloatField()),
                ('initiated_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 17, 21, 57, 82829))),
                ('confirmation_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 17, 21, 57, 82851))),
                ('payment_status', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_amount', models.FloatField()),
                ('actual_amount', models.FloatField()),
                ('purchase_status', models.CharField(max_length=30)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 4, 17, 21, 57, 80430))),
                ('customer', models.ForeignKey(related_name=b'user_who_purchased', to='user_accounts.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='payments',
            name='purchase',
            field=models.ForeignKey(related_name=b'purchase_id_payment', to='booking.Purchase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='purchase',
            field=models.ForeignKey(related_name=b'purchase_id', to='booking.Purchase'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='studio',
            field=models.ForeignKey(related_name=b'booked_on_studio', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='user',
            field=models.ForeignKey(related_name=b'booked_by_user', to='user_accounts.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookedmessagesend',
            name='booking',
            field=models.ForeignKey(related_name=b'booking_id', to='booking.BookingDetails'),
            preserve_default=True,
        ),
    ]
