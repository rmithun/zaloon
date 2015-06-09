# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0014_auto_20150606_0714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studioprofile',
            old_name='is_closed',
            new_name='is_not_closed',
        ),
        migrations.AddField(
            model_name='studioaccountdetails',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_account_detail', default=1, to='studios.Studio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studiocloseddetails',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_closed_details', default=1, to='studios.Studio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studioclosedfromtill',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_long_closed_details', default=1, to='studios.Studio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studioinvoices',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_invoice_detail', default=1, to='studios.Studio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studiopasswordreset',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_pwd_reset', default=1, to='studios.Studio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studiopayment',
            name='studio',
            field=models.ForeignKey(related_name=b'studio_payment_detail', default=1, to='studios.Studio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 742238)),
        ),
        migrations.AlterField(
            model_name='closedates',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 747358)),
        ),
        migrations.AlterField(
            model_name='paymentmodes',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 744475)),
        ),
        migrations.AlterField(
            model_name='service',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 738615)),
        ),
        migrations.AlterField(
            model_name='servicetype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 738114)),
        ),
        migrations.AlterField(
            model_name='studio',
            name='last_signout_datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 739148), null=True),
        ),
        migrations.AlterField(
            model_name='studioaccountdetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 745054)),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'studio_amenities', to='studios.Studio'),
        ),
        migrations.AlterField(
            model_name='studioamenities',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 742716)),
        ),
        migrations.AlterField(
            model_name='studiocloseddetails',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 747823)),
        ),
        migrations.AlterField(
            model_name='studioclosedfromtill',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 748372)),
        ),
        migrations.AlterField(
            model_name='studiogroup',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 740304)),
        ),
        migrations.AlterField(
            model_name='studioinvoices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 746366)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='password_changed_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 746841)),
        ),
        migrations.AlterField(
            model_name='studiopasswordreset',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 746882)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='paid_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 745650)),
        ),
        migrations.AlterField(
            model_name='studiopayment',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 745690)),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'pic_of_studio', to='studios.Studio'),
        ),
        migrations.AlterField(
            model_name='studiopicture',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 748985)),
        ),
        migrations.AlterField(
            model_name='studioprofile',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 741394)),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'studio_detail_for_activity', to='studios.Studio'),
        ),
        migrations.AlterField(
            model_name='studioservices',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 743371)),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='studio_profile',
            field=models.ForeignKey(related_name=b'studio_staff_count', to='studios.Studio'),
        ),
        migrations.AlterField(
            model_name='studiostaffcounts',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 743934)),
        ),
        migrations.AlterField(
            model_name='studiotype',
            name='updated_date_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 7, 41, 6, 739643)),
        ),
    ]
