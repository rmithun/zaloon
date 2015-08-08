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
            name='Amenities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amenity_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 859623))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CloseDates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('closed_on_day', models.CharField(max_length=25)),
                ('closed_on_desc', models.CharField(max_length=50)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 864877))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 861896))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=100)),
                ('min_duration', models.IntegerField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 854961))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_type_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 854398))),
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
                ('last_signout_datetime', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 855493), null=True)),
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
                ('min_deposit', models.PositiveIntegerField()),
                ('max_deposit', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 862492))),
                ('mode_of_payment', models.ForeignKey(related_name=b'payment_mode_for_studio_account', to='studios.PaymentModes')),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 856145))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioAmenities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 860103))),
                ('amenity', models.ForeignKey(related_name=b'amenity_available', to='studios.Amenities')),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 865366))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 865922))),
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
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('landline_no_1', models.CharField(max_length=40, null=True)),
                ('landline_no_2', models.CharField(max_length=40, null=True)),
                ('mobile_no_1', models.CharField(max_length=40)),
                ('mobile_no_2', models.CharField(max_length=40, null=True)),
                ('contact_person_1', models.CharField(max_length=75)),
                ('contact_person_2', models.CharField(max_length=75, null=True)),
                ('primary_email', models.CharField(max_length=50)),
                ('secondary_email', models.CharField(max_length=50)),
                ('total_branches', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 857186))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 863740))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 857696))),
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
                ('password_changed_date', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 864231))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 864274))),
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
                ('paid_date', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 863106))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 863148))),
                ('mode_of_payment', models.ForeignKey(related_name=b'payment_mode_for_studio_payments', to='studios.PaymentModes')),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 866443))),
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
                ('landmark', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=40)),
                ('area', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=40)),
                ('landline_no_1', models.CharField(max_length=40, null=True)),
                ('landline_no_2', models.CharField(max_length=40, null=True)),
                ('incharge_mobile_no', models.CharField(max_length=40)),
                ('contact_mobile_no', models.CharField(max_length=40, null=True)),
                ('in_charge_person', models.CharField(max_length=75)),
                ('contact_person', models.CharField(max_length=75, null=True)),
                ('opening_at', models.TimeField()),
                ('closing_at', models.TimeField()),
                ('is_active', models.BooleanField(default=1)),
                ('is_closed', models.BooleanField(default=0)),
                ('daily_studio_closed_from', models.TimeField()),
                ('daily_studio_closed_till', models.TimeField()),
                ('thumbnail', models.ImageField(upload_to=b'img_gallery')),
                ('is_ac', models.BooleanField(default=0)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 858708))),
                ('latitude', models.CharField(max_length=30)),
                ('longitude', models.CharField(max_length=30)),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 860705))),
                ('service', models.ForeignKey(related_name=b'service_in_studio', to='studios.Service')),
                ('studio_profile', models.ForeignKey(related_name=b'studio_detail_for_activity', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudioStaffCounts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('normal_day', models.PositiveIntegerField()),
                ('holiday', models.PositiveIntegerField()),
                ('festive_season', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 861267))),
                ('studio_profile', models.OneToOneField(related_name=b'studio_staff_count', to='studios.StudioProfile')),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 23, 12, 15, 21, 856605))),
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
            model_name='studioclosedfromtill',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_long_closed_details', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studiocloseddetails',
            name='studio',
            field=models.OneToOneField(related_name=b'studio_closed_details', to='studios.StudioProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioamenities',
            name='studio_profile',
            field=models.OneToOneField(related_name=b'studio_amenities', to='studios.StudioProfile'),
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
