# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 20:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20160918_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='alpha3',
            field=models.CharField(help_text='The three letter country code for this country.', max_length=3, null=True),
        ),
    ]
