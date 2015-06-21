# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_auto_20150620_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedMessageSent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(null=True)),
                ('mobile_no', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('is_successful', models.BooleanField(default=0)),
                ('type_of_message', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=25)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 467166))),
                ('booking', models.ForeignKey(related_name=b'booking_id', to='booking.BookingDetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bookedmessagesend',
            name='booking',
        ),
        migrations.DeleteModel(
            name='BookedMessageSend',
        ),
        migrations.RenameField(
            model_name='bookingdetails',
            old_name='reminder_sent',
            new_name='notification_send',
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 465634)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 467707)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 470018)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 470583)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 469445)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 468160)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 468138)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 464645)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 6, 20, 19, 35, 54, 466494)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 466532)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 468863)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 35, 54, 471136)),
        ),
    ]
