# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0007_auto_20150606_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=20)),
                ('status_code', models.CharField(max_length=20)),
                ('amount_refunded', models.FloatField()),
                ('initiated_date_time', models.DateTimeField(verbose_name=datetime.datetime(2015, 6, 12, 12, 6, 24, 208138))),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 208175))),
                ('booking', models.ForeignKey(related_name=b'refund_of_booking', to='booking.BookingDetails')),
                ('purchase', models.ForeignKey(related_name=b'refund_from_purchase', to='booking.Purchase')),
                ('user', models.ForeignKey(related_name=b'refund_to_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bookedmessagesend',
            name='mobile_no',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='status_code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='status_code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedmessagesend',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 208802)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='purchase',
            field=models.ForeignKey(related_name=b'purchase_id', to='booking.Purchase', null=True),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 207443)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 209480)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 209954)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 209934)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 206776)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 12, 12, 6, 24, 210580)),
        ),
    ]
