# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0002_auto_20150625_1136'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedMessageSent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(null=True)),
                ('mobile_no', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=60, null=True)),
                ('is_successful', models.BooleanField(default=0)),
                ('type_of_message', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=25)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 947079))),
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
                ('appointment_start_time', models.TimeField()),
                ('appointment_end_time', models.TimeField(null=True)),
                ('booking_code', models.CharField(max_length=25)),
                ('status_code', models.CharField(max_length=10)),
                ('booking_status', models.CharField(max_length=30)),
                ('notification_send', models.BooleanField(default=0)),
                ('is_valid', models.BooleanField(default=1)),
                ('total_duration', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 945369))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 947672))),
                ('booking', models.ForeignKey(related_name=b'service_booked_with', to='booking.BookingDetails')),
                ('service', models.ForeignKey(related_name=b'service_booked', to='studios.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyReminder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_no', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=1)),
                ('message', models.TextField()),
                ('service_updated', models.CharField(max_length=30)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 950121))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 950717))),
                ('booking', models.ForeignKey(related_name=b'hr_reminder_for_booking', to='booking.BookingDetails')),
                ('user', models.ForeignKey(related_name=b'hr_for_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MerchantDailyReportStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_date', models.DateField(default=datetime.date(2015, 6, 25))),
                ('report', models.FileField(upload_to=b'reports/%Y/%m/%d')),
                ('mail_sent', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 949510))),
                ('studio', models.ForeignKey(related_name=b'studio_report', to='studios.StudioProfile')),
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
                ('initiated_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 948129))),
                ('confirmation_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 948153))),
                ('payment_status', models.CharField(max_length=30)),
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
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_amount', models.FloatField()),
                ('actual_amount', models.FloatField()),
                ('purchase_status', models.CharField(max_length=30)),
                ('status_code', models.CharField(max_length=10)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 944301))),
                ('customer', models.ForeignKey(related_name=b'user_who_purchased', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=20)),
                ('status_code', models.CharField(max_length=20)),
                ('amount_refunded', models.FloatField()),
                ('initiated_date_time', models.DateTimeField(verbose_name=datetime.datetime(2015, 6, 25, 11, 36, 31, 946364))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 946409))),
                ('booking', models.ForeignKey(related_name=b'refund_of_booking', to='booking.BookingDetails')),
                ('purchase', models.ForeignKey(related_name=b'refund_from_purchase', to='booking.Purchase')),
                ('user', models.ForeignKey(related_name=b'refund_to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioReviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField()),
                ('comment', models.TextField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 948890))),
                ('booking', models.ForeignKey(related_name=b'reviewed_on_booking', to='booking.BookingDetails')),
                ('studio_profile', models.ForeignKey(related_name=b'studio_review', to='studios.StudioProfile')),
                ('user', models.ForeignKey(related_name=b'reviewed_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThanksMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=60)),
                ('status', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=30)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 25, 11, 36, 31, 951297))),
                ('booking', models.ForeignKey(related_name=b'tm_for_booking', to='booking.BookingDetails')),
                ('user', models.ForeignKey(related_name=b'tm_for_user', to=settings.AUTH_USER_MODEL)),
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
            name='promo',
            field=models.ForeignKey(related_name=b'applied_promo_code', to='booking.Promo', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='purchase',
            field=models.ForeignKey(related_name=b'purchase_id', to='booking.Purchase', null=True),
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
            field=models.ForeignKey(related_name=b'booked_by_user', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bookedmessagesent',
            name='booking',
            field=models.ForeignKey(related_name=b'booking_id', to='booking.BookingDetails'),
            preserve_default=True,
        ),
    ]
