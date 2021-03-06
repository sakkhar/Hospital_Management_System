# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 06:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('blood_group', models.CharField(blank=True, choices=[('O', 'O Positive'), ('O', 'O Negetive)'), ('AB', 'AB Positive'), ('AB', 'AB Negetive'), ('A', 'A Positive'), ('A', 'A Negetive'), ('B', 'B Positive'), ('B', 'B Negetive')], max_length=1)),
                ('birth_date', models.DateField()),
                ('image', models.ImageField(upload_to=None)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
