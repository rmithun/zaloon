# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInvites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 9, 20, 2, 23, 59, 689955))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField(null=True)),
                ('sex', models.CharField(max_length=10)),
                ('city_state', models.CharField(max_length=60, null=True)),
                ('area', models.CharField(max_length=40, null=True)),
                ('facebook_id', models.CharField(max_length=50, blank=True)),
                ('mobile', models.CharField(max_length=25, null=True)),
                ('service_updated', models.CharField(max_length=25, null=True)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 9, 20, 2, 23, 59, 689062))),
                ('user_acc', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
