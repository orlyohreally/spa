# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-15 08:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_auto_20170214_1928'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='main_task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='spa.Task'),
        ),
    ]
