# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0006_auto_20150703_2128'),
        ('booking', '0003_auto_20150702_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coupon_code', models.CharField(max_length=10)),
                ('expiry_date', models.DateTimeField()),
                ('for_all_studios', models.BooleanField()),
                ('is_one_time', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('coupon_type', models.CharField(max_length=10)),
                ('discount_value', models.PositiveIntegerField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 532344))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 532999))),
                ('coupon', models.ForeignKey(related_name=b'coupon_for_studio', to='booking.Coupon')),
                ('studio', models.ForeignKey(related_name=b'studio_have_coupon', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bookingdetails',
            name='promo',
        ),
        migrations.DeleteModel(
            name='Promo',
        ),
        migrations.AddField(
            model_name='bookingdetails',
            name='coupon',
            field=models.ForeignKey(related_name=b'applied_promo_code', to='booking.Coupon', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 535246)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 533755)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 535911)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 7, 3)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 541940)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 538214)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 540656)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='report_date',
            field=models.DateField(default=datetime.date(2015, 7, 3)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 537631)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 536394)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 536370)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 531768)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 7, 3, 21, 28, 43, 534574)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 534614)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 537022)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 3, 21, 28, 43, 541379)),
        ),
    ]
