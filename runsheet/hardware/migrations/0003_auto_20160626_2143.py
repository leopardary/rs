# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 04:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0002_auto_20160626_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomtuner',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='depchamber',
            name='configure_start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 868000, tzinfo=utc), verbose_name='Configuration starting time'),
        ),
        migrations.AlterField(
            model_name='faceplate',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gasbox',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lowerblockerplate',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherparts',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pedestalheater',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='toptuner',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upperblockerplate',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 43, 22, 759000, tzinfo=utc)),
        ),
    ]
