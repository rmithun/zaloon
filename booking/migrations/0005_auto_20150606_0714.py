# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0014_auto_20150606_0714'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_auto_20150606_0646'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudioReviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField()),
                ('comments', models.TextField()),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 595619))),
                ('service', models.ForeignKey(related_name=b'reviewed_the_service', to='studios.Service', null=True)),
                ('studio_profile', models.ForeignKey(related_name=b'studio_review', to='studios.StudioProfile')),
                ('user', models.ForeignKey(related_name=b'reviewed_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 593927)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 593285)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 594449)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 594896)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 594876)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 14, 23, 592643)),
        ),
    ]
