# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20171011_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admission',
            name='age',
            field=models.IntegerField(blank=True, max_length=100, null=True),
        ),
    ]
