# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_name', models.CharField(max_length=25)),
                ('min_duration', models.IntegerField()),
                ('is_active', models.BooleanField(default=1)),
                ('unit_price', models.IntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 713336))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_type_name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 712778))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookedMessageSend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('is_successful', models.BooleanField(default=0)),
                ('type_of_message', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=25)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 714657))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BookingDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_booked', models.IntegerField()),
                ('scheduled_at', models.DateTimeField()),
                ('booking_code', models.CharField(max_length=25)),
                ('expires_on', models.DateTimeField()),
                ('booking_status', models.BooleanField(default=1)),
                ('reminder_sent', models.BooleanField(default=0)),
                ('user_arrived', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 713899))),
                ('activity', models.ForeignKey(related_name=b'activity_booked', to='booking.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bookedmessagesend',
            name='booking',
            field=models.ForeignKey(related_name=b'booking_id', to='booking.BookingDetails'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(related_name=b'type_of_activity', to='booking.ActivityType'),
            preserve_default=True,
        ),
    ]
