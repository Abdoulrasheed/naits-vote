# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_electionsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionsession',
            name='ends_on',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='electionsession',
            name='starts_on',
            field=models.TimeField(blank=True, null=True),
        ),
    ]