# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloseDates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closed_on_day', models.CharField(max_length=25)),
                ('closed_on_desc', models.CharField(max_length=50)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 115389))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=100, db_index=True)),
                ('min_duration', models.IntegerField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_for', models.IntegerField(default=1)),
                ('service_updated', models.CharField(default=b'Admin', max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 101889))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=100, db_index=True)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(default=b'Admin', max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 100783))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(unique=True, max_length=254, db_index=True)),
                ('is_active', models.BooleanField(default=False)),
                ('last_password_reset_datetime', models.DateTimeField(null=True)),
                ('last_signout_datetime', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 102793), null=True)),
            ],
            options={
                'abstract': False,
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
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 111638))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioAddRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('studio_name', models.CharField(max_length=30)),
                ('area', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=60)),
                ('service_updated', models.CharField(max_length=30)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 103687))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 116145))),
                ('closed_on', models.ForeignKey(related_name=b'studio_close_dates', to='studios.CloseDates')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(default=b'Chennai', max_length=40)),
                ('country', models.CharField(default=b'India', max_length=40)),
                ('contact_no', models.CharField(max_length=40, blank=True)),
                ('primary_email', models.CharField(max_length=50, blank=True)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 105223))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioInvoices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount_to_be_paid', models.FloatField()),
                ('total_booking', models.PositiveIntegerField()),
                ('fee_amount', models.FloatField()),
                ('invoice_date', models.DateField(default=datetime.date(2015, 10, 16))),
                ('total_booking_amount', models.FloatField()),
                ('service_tax_amount', models.FloatField()),
                ('service_updated', models.CharField(max_length=50)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 113574))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind_desc', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=1)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 106134))),
                ('service_updated', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioPasswordReset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password_changed_date', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 114371))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 114442))),
                ('studio', models.ForeignKey(related_name=b'studio_pwd_reset', to='studios.Studio')),
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
                ('paid_date', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 112502))),
                ('disputed', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 112596))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(null=True, upload_to=b'img_gallery', blank=True)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 116983))),
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
                ('landmark', models.CharField(max_length=200, blank=True)),
                ('city', models.CharField(default=b'Chennai', max_length=40)),
                ('country', models.CharField(default=b'India', max_length=40)),
                ('area', models.CharField(max_length=100)),
                ('state', models.CharField(default=b'Tamil nadu', max_length=40)),
                ('search_field_1', models.CharField(max_length=200)),
                ('search_field_2', models.CharField(max_length=200)),
                ('landline_no_1', models.CharField(max_length=40, null=True, blank=True)),
                ('landline_no_2', models.CharField(max_length=40, null=True, blank=True)),
                ('incharge_mobile_no', models.CharField(max_length=40)),
                ('contact_mobile_no', models.CharField(max_length=40, null=True, blank=True)),
                ('in_charge_person', models.CharField(max_length=75)),
                ('contact_person', models.CharField(max_length=75, null=True, blank=True)),
                ('opening_at', models.TimeField(null=True)),
                ('closing_at', models.TimeField(null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('is_closed', models.BooleanField(default=0)),
                ('daily_studio_closed_from', models.TimeField(null=True, blank=True)),
                ('daily_studio_closed_till', models.TimeField(null=True, blank=True)),
                ('thumbnail', models.ImageField(upload_to=b'img_gallery')),
                ('is_ac', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 107705))),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
                ('has_online_payment', models.BooleanField(default=1)),
                ('commission_percent', models.IntegerField(default=10)),
                ('has_service_tax', models.IntegerField(default=0)),
                ('studio', models.OneToOneField(related_name=b'studio_login', to='studios.Studio')),
                ('studio_group', models.ForeignKey(related_name=b'studio_of_group', to='studios.StudioGroup')),
                ('studio_kind', models.ForeignKey(related_name=b'kind_of_studio', to='studios.StudioKind')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioServices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=1)),
                ('mins_takes', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 110648))),
                ('service', models.ForeignKey(related_name=b'service_in_studio', to='studios.Service')),
                ('studio_profile', models.ForeignKey(related_name=b'studio_detail_for_activity', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioServiceTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 109537))),
                ('service_type', models.ForeignKey(related_name=b'service_type_in_studio', to='studios.ServiceType')),
                ('studio_profile', models.ForeignKey(related_name=b'studio_detail_for_service_type', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type_desc', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 10, 16, 0, 20, 18, 104424))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='studio_type',
            field=models.ForeignKey(related_name=b'studio_type', to='studios.StudioType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studiopicture',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'pic_of_studio', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studiopayment',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_payment_detail', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioinvoices',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_invoice_detail', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studiocloseddetails',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_closed_details', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioaccountdetails',
            name='studio',
            field=models.OneToOneField(related_name=b'studio_account_detail', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='service',
            name='service_type',
            field=models.ForeignKey(related_name=b'type_of_service', to='studios.ServiceType'),
            preserve_default=True,
        ),
    ]
