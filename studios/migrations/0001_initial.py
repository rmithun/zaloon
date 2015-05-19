# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20150516_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='CloseDates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closed_on_day', models.CharField(max_length=25)),
                ('closed_on_desc', models.CharField(max_length=50)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 422715))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PaymentModes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mode', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=75)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 417329))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioAccountDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bank_name', models.CharField(max_length=120)),
                ('bank_branch', models.CharField(max_length=120)),
                ('bank_ifsc', models.CharField(max_length=25)),
                ('bank_city', models.CharField(max_length=40)),
                ('bank_acc_number', models.CharField(max_length=120)),
                ('min_deposit', models.PositiveIntegerField()),
                ('max_deposit', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 418319))),
                ('mode_of_payment', models.ForeignKey(related_name=b'payment_mode_for_studio_account', to='studios.PaymentModes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioActivities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 416552))),
                ('activity', models.ForeignKey(related_name=b'activity_in_studio', to='booking.Activity')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioActivityTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 415564))),
                ('activity_type', models.ForeignKey(related_name=b'type_of_activity_in_studio', to='booking.ActivityType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioBlockedDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('blocked_from', models.DateTimeField()),
                ('blocked_till', models.DateTimeField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 421809))),
                ('activity', models.ForeignKey(related_name=b'activity_blocked_in_studio', to='booking.Activity')),
                ('booking', models.ForeignKey(related_name=b'booking_id_for_studio', to='booking.BookingDetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioClosedDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 423458))),
                ('closed_on', models.ForeignKey(related_name=b'studio_close_dates', to='studios.CloseDates')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioClosedFromTill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closed_from_date', models.DateField()),
                ('closed_till_date', models.DateField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 424209))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioDailyInvoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('booked_date', models.DateTimeField()),
                ('count_booked', models.PositiveIntegerField()),
                ('is_filled', models.NullBooleanField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 425246))),
                ('activity_booked', models.ForeignKey(related_name=b'daily_invoice_booked_activity', to='booking.Activity')),
                ('booking', models.ForeignKey(related_name=b'booking_for_daily_invoice', to='booking.BookingDetails')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioInvoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_to_be_paid', models.PositiveIntegerField()),
                ('last_payment_amount', models.PositiveIntegerField()),
                ('last_payment_date', models.DateTimeField()),
                ('payment_requested', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 420084))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioPasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password_changed_date', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 420933))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 420999))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioPayment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_paid', models.PositiveIntegerField()),
                ('paid_by', models.CharField(max_length=120)),
                ('paid_date', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 419196))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 419259))),
                ('mode_of_payment', models.ForeignKey(related_name=b'payment_mode_for_studio_payments', to='studios.PaymentModes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('address_1', models.CharField(max_length=200)),
                ('address_2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('area', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('landline_no_1', models.CharField(max_length=40, null=True)),
                ('landline_no_2', models.CharField(max_length=40, null=True)),
                ('mobile_no_1', models.CharField(max_length=40)),
                ('mobile_no_2', models.CharField(max_length=40, null=True)),
                ('contact_person_1', models.CharField(max_length=75)),
                ('contact_person_2', models.CharField(max_length=75, null=True)),
                ('opening_at', models.PositiveSmallIntegerField()),
                ('closing_at', models.PositiveSmallIntegerField()),
                ('is_active', models.BooleanField(default=1)),
                ('contract_start_date', models.DateTimeField()),
                ('contract_end_date', models.DateTimeField()),
                ('last_login', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 414223))),
                ('first_login', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 414260))),
                ('is_closed', models.BooleanField(default=1)),
                ('daily_studio_closed_from', models.PositiveSmallIntegerField()),
                ('daily_studio_closed_till', models.PositiveSmallIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 16, 16, 27, 55, 414387))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
