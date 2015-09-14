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
            name='CouponForUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField()),
                ('expiry_date', models.DateField()),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 698579))),
                ('coupon', models.ForeignKey(related_name=b'coupon_for_user', to='booking.Coupon')),
                ('user', models.ForeignKey(related_name=b'user_have_coupon', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coupon',
            name='user_based',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bookedmessagesent',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 704235)),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 700841)),
        ),
        migrations.AlterField(
            model_name='bookingservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 705097)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 697657)),
        ),
        migrations.AlterField(
            model_name='couponforstudios',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 699469)),
        ),
        migrations.AlterField(
            model_name='dailybookingconfirmation',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 711670)),
        ),
        migrations.AlterField(
            model_name='dailyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 708907)),
        ),
        migrations.AlterField(
            model_name='hourlyreminder',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 709888)),
        ),
        migrations.AlterField(
            model_name='merchantdailyreportstatus',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 707810)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='confirmation_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 705871)),
        ),
        migrations.AlterField(
            model_name='payments',
            name='initiated_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 705831)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 696674)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='initiated_date_time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2015, 9, 8, 0, 2, 21, 703022)),
        ),
        migrations.AlterField(
            model_name='refund',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 703087)),
        ),
        migrations.AlterField(
            model_name='reviewlink',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 712497)),
        ),
        migrations.AlterField(
            model_name='rzpayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 702101)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 706864)),
        ),
        migrations.AlterField(
            model_name='thanksmail',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 8, 0, 2, 21, 710798)),
        ),
    ]
