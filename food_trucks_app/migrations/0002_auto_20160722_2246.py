# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-22 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_trucks_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilefoodtrucks',
            name='xcoordi',
        ),
        migrations.RemoveField(
            model_name='mobilefoodtrucks',
            name='ycoordi',
        ),
    ]
