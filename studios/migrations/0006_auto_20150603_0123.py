# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0005_auto_20150530_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amenity_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=1)),
                ('service_updated', models.CharField(max_length=25)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 515430))),
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
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 515907))),
                ('amenity', models.ForeignKey(related_name=b'amenity_available', to='studios.Amenities')),
                ('studio_profile', models.ForeignKey(related_name=b'studio_amenities', to='studios.StudioProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='is_ac',
            field=models.BooleanField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='serve_type',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='thumbnail',
            field=models.ImageField(default=1, upload_to=b'img_gallery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studioreviews',
            name='is_active',
            field=models.BooleanField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 520244)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 517637)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 511896)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 511393)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 512435), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 518184)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 520678)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 521164)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 513585)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 519260)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 519779)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 519821)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 518718)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 518756)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 522372)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 514653)),
        ),
        migrations.AlterField(
            model_name='studioreviews',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 521713)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 516467)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 517135)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 3, 1, 23, 55, 512952)),
        ),
    ]
