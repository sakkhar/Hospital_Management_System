# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor_hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed_Allotment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=100)),
            ],
        ),
    ]
