# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0012_auto_20150620_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinvites',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 36, 17, 787134)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 20, 19, 36, 17, 786498)),
        ),
    ]
