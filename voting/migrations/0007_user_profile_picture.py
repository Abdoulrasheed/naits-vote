# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-29 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0006_delete_electionsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(blank=True, help_text=b'upload your profile picture', null=True, upload_to=b'profile_pictures'),
        ),
    ]