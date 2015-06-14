# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0009_auto_20150612_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInvites',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=75)),
                ('date', models.DateTimeField(default=datetime.datetime(2015, 6, 14, 23, 47, 43, 70666))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 14, 23, 47, 43, 70027)),
        ),
    ]
