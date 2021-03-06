# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-03-14 00:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20180306_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='housingresources',
            name='quality',
            field=models.IntegerField(choices=[(0, '\u5426'), (1, '\u662f')], default=0, verbose_name='\u662f\u5426\u4e3a\u54c1\u8d28\u623f\u6e90'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='renthousemeet',
            name='comp_meet_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 14, 0, 6, 42, 37322), verbose_name='\u5df2\u9884\u7ea6\u65f6\u95f4'),
        ),
    ]
