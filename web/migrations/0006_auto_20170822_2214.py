# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 22:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20170717_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bank_acount',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='\u94f6\u884c\u5361\u4fe1\u606f'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birbath',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u751f\u65e5'),
        ),
    ]