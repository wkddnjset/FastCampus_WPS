# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='youtubeuser',
            options={'verbose_name': '사용자', 'verbose_name_plural': '사용자들'},
        ),
    ]
