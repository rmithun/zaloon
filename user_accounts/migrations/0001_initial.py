# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('is_active', models.BooleanField(default=1)),
                ('active_till_date', models.DateTimeField(null=True)),
                ('price', models.IntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 715182))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlanDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_in_plan', models.IntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 717114))),
                ('activity', models.ForeignKey(related_name=b'activity_in_plan', to='booking.Activity')),
                ('activity_type', models.ForeignKey(related_name=b'type_of_activity_in_plan', to='booking.ActivityType')),
                ('plan', models.ForeignKey(related_name=b'plan_details', to='user_accounts.Plan')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserActivitiesList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count_available', models.IntegerField()),
                ('count_used', models.IntegerField()),
                ('total_count', models.IntegerField()),
                ('expires_on', models.DateTimeField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 716460))),
                ('is_active', models.BooleanField(default=1)),
                ('activity', models.ForeignKey(related_name=b'activity_available_for_user', to='booking.Activity')),
                ('activity_type', models.ForeignKey(related_name=b'type_of_activity_available_for_user', to='booking.ActivityType')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('sex', models.NullBooleanField()),
                ('city_state', models.CharField(max_length=60, null=True)),
                ('area', models.CharField(max_length=40, null=True)),
                ('facebook_id', models.CharField(max_length=50, blank=True)),
                ('mobile', models.CharField(max_length=25, null=True)),
                ('signup_date', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 715741))),
                ('last_login', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 715759))),
                ('service_updated', models.CharField(max_length=25, null=True)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 5, 12, 10, 57, 31, 715790))),
                ('plan', models.ForeignKey(related_name=b'user_in_plan', to='user_accounts.Plan', null=True)),
                ('user_acc', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='useractivitieslist',
            name='user',
            field=models.ForeignKey(related_name=b'user_activity_availablilty', to='user_accounts.UserProfile'),
            preserve_default=True,
        ),
    ]
