# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-22 21:33
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileFoodTrucks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationid', models.IntegerField()),
                ('applicant', models.CharField(max_length=254)),
                ('facility', models.CharField(max_length=254)),
                ('block', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('permit', models.CharField(max_length=254)),
                ('status', models.CharField(max_length=254)),
                ('fooditems', models.CharField(max_length=254)),
                ('xcoordi', models.FloatField()),
                ('ycoordi', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('dayshours', models.CharField(max_length=254)),
                ('permit_exp', models.CharField(max_length=254)),
                ('location', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=-1)),
            ],
        ),
    ]