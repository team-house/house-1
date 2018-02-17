# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-12 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_del', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5220\u9664')),
                ('is_valid', models.BooleanField(default=True, verbose_name='\u662f\u5426\u53ef\u7528')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('module', models.CharField(default='', max_length=255, verbose_name='\u6a21\u5757\u540d\u79f0')),
                ('module_cn', models.CharField(default='', max_length=255, verbose_name='\u6a21\u5757\u4e2d\u6587\u540d\u79f0')),
                ('permission_ids', models.CharField(default='', max_length=255, verbose_name='\u6743\u9650\u9009\u9879')),
            ],
            options={
                'verbose_name': '\u8bbf\u95ee\u63a7\u5236\u5217\u8868',
                'verbose_name_plural': '\u8bbf\u95ee\u63a7\u5236\u5217\u8868',
                'permissions': (('view_module', '\u67e5\u770b'), ('add_module', '\u6dfb\u52a0'), ('edit_module', '\u7f16\u8f91'), ('delete_module', '\u5220\u9664'), ('active_module', '\u542f\u7528\u7981\u7528'), ('move_module', '\u4e0a\u79fb\u4e0b\u79fb')),
            },
        ),
    ]
