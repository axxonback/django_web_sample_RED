# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-30 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(),
        ),
    ]
