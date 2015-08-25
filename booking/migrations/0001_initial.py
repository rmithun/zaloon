# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedMessageSent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField(null=True)),
                ('is_successful', models.BooleanField(default=0)),
                ('type_of_message', models.CharField(max_length=25)),
                ('mode', models.CharField(max_length=25)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 301414))),
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
                ('appointment_end_time', models.TimeField()),
                ('mobile_no', models.CharField(max_length=30, null=True)),
                ('booking_code', models.CharField(max_length=25)),
                ('status_code', models.CharField(max_length=10)),
                ('booking_status', models.CharField(max_length=30)),
                ('notification_send', models.BooleanField(default=0)),
                ('is_valid', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 299235))),
                ('is_reviewed', models.BooleanField(default=0)),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 301966))),
                ('booking', models.ForeignKey(related_name=b'service_booked_with', to='booking.BookingDetails')),
                ('service', models.ForeignKey(related_name=b'service_booked', to='studios.Service')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coupon_code', models.CharField(max_length=10)),
                ('expiry_date', models.DateTimeField()),
                ('for_all_studios', models.BooleanField()),
                ('maximum_discount', models.PositiveIntegerField()),
                ('is_one_time', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('coupon_type', models.CharField(max_length=10)),
                ('discount_value', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 297945))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CouponForStudios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 298489))),
                ('coupon', models.ForeignKey(related_name=b'coupon_for_studio', to='booking.Coupon')),
                ('studio', models.ForeignKey(related_name=b'studio_have_coupon', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DailyBookingConfirmation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report_date', models.DateField(default=datetime.date(2015, 8, 25))),
                ('booking_pdf', models.FileField(upload_to=b'reports/%Y/%m/%d')),
                ('mail_sent', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 308126))),
                ('studio', models.ForeignKey(related_name=b'studio_confirmed_booking', to='studios.StudioProfile')),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 306181))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 306804))),
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
                ('report_date', models.DateField(default=datetime.date(2015, 8, 25))),
                ('report', models.FileField(upload_to=b'reports/%Y/%m/%d')),
                ('mail_sent', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 305591))),
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
                ('initiated_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 304241))),
                ('confirmation_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 304272))),
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
                ('status_code', models.CharField(max_length=10)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 297341))),
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
                ('initiated_date_time', models.DateTimeField(verbose_name=datetime.datetime(2015, 8, 25, 17, 25, 19, 300734))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 300778))),
                ('booking', models.ForeignKey(related_name=b'refund_of_booking', to='booking.BookingDetails')),
                ('purchase', models.ForeignKey(related_name=b'refund_from_purchase', to='booking.Purchase')),
                ('user', models.ForeignKey(related_name=b'refund_to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ReviewLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_reviewed', models.BooleanField(default=0)),
                ('link_code', models.CharField(max_length=50)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 308642))),
                ('service_updated', models.CharField(max_length=30)),
                ('booking', models.ForeignKey(related_name=b'review_link_of_booking', to='booking.BookingDetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RZPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rzp_payment_id', models.CharField(max_length=100)),
                ('rzp_status', models.CharField(max_length=30)),
                ('service_updated', models.CharField(max_length=25)),
                ('refund_id', models.CharField(max_length=100, null=True)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 300157))),
                ('purchase', models.ForeignKey(related_name=b'purchase_id_rzp', to='booking.Purchase')),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 304965))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 8, 25, 17, 25, 19, 307562))),
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
            name='coupon',
            field=models.ForeignKey(related_name=b'applied_promo_code', to='booking.Coupon', null=True),
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
