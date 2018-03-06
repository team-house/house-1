# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-05 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0008_auto_20180219_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentHouseMeet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('meet_time', models.DateTimeField(auto_now=True, verbose_name='\u9884\u7ea6\u65f6\u95f4')),
                ('rent_house', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.RentHouse', verbose_name='\u6c42\u79df')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237')),
            ],
            options={
                'verbose_name': '\u6c42\u79df\u9884\u7ea6',
                'verbose_name_plural': '\u6c42\u79df\u9884\u7ea6',
            },
        ),
    ]
