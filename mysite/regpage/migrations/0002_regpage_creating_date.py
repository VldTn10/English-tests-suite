# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-27 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='regpage',
            name='creating_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
