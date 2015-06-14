# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0018_auto_20150612_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudioKind',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('kind_desc', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=1)),
                ('updated_date_time', models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 13034))),
                ('service_updated', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studioprofile',
            name='studio_kind',
            field=models.ForeignKey(related_name=b'kind_of_studio', default=1, to='studios.StudioKind'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 14860)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 19814)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 16996)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 10780)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 10288)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 11305), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 17555)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 15432)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 20271)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 20890)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 12515)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 18865)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 19334)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 19372)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 18260)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 18298)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 21407)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 13907)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 15979)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 16513)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 13, 13, 45, 50, 11808)),
        ),
    ]
