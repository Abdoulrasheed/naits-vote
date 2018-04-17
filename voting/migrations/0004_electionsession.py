# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_user_hall_of_residence'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_on', models.DateTimeField(blank=True, null=True)),
                ('ends_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
