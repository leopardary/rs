# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 04:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomtuner',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='depchamber',
            name='configure_start_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 836000, tzinfo=utc), verbose_name='Configuration starting time'),
        ),
        migrations.AlterField(
            model_name='faceplate',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='gasbox',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lowerblockerplate',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='otherparts',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pedestalheater',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='toptuner',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upperblockerplate',
            name='entry_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 27, 4, 39, 8, 727000, tzinfo=utc)),
        ),
    ]