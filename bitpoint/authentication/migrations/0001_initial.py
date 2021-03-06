# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-14 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('ID_Number', models.CharField(max_length=15, null=True, unique=True)),
                ('level', models.CharField(choices=[(b'100', b'100'), (b'200', b'200'), (b'300', b'300'), (b'400', b'400'), (b'500', b'500'), (b'Graduated', b'Graduated')], max_length=9)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('gender', models.CharField(blank=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')], max_length=50, null=True, verbose_name='Gender')),
                ('hall_of_residence', models.CharField(blank=True, choices=[(b'OFF CAMPUS', b'OFF CAMPUS'), (b'KABIRU UMAR', b'KABIRU UMAR'), (b'USMAN NAGOGGO', b'USMAN NAGOGGO'), (b'NANA ASMAU', b'NANA ASMAU'), (b'OBA ADETOLA', b'OBA ADETOLA'), (b'NEW HOSTEL - MALE', b'NEW HOSTEL - MALE'), (b'NEW HOSTEL - FEMALE', b'NEW HOSTEL - FEMALE')], max_length=50, null=True, verbose_name='Hall')),
                ('state_of_origin', models.CharField(blank=True, choices=[(b'Abia', b'Abia'), (b'Adamawa', b'Adamawa')], max_length=50, null=True, verbose_name='State')),
                ('town', models.CharField(blank=True, choices=[(b'Yola', b'Yola'), (b'Jimeta', b'Jimeta')], max_length=50, null=True, verbose_name='Local Government')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, help_text='e.g abcd@example.com', max_length=254, null=True, verbose_name='Email')),
                ('facebook_id', models.CharField(blank=True, help_text='Your facebook id e.g abdulrasheed.ibrahim.756', max_length=50, null=True, verbose_name='Facebook')),
                ('twitter_handler', models.CharField(blank=True, help_text='Your twitter handler e.g @abdulrasheed1', max_length=50, null=True, verbose_name='Twitter handler')),
                ('instagram_id', models.CharField(blank=True, help_text='Your instagram ID e.g abdoul_rasheed', max_length=50, null=True, verbose_name='Instagram')),
                ('pinterest', models.CharField(blank=True, help_text='Your pin ID e.g example', max_length=50, null=True, verbose_name='Pinterest')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can login to this site as admin.', verbose_name='Site staff')),
                ('is_d_staff', models.BooleanField(default=False, help_text='Designates whether the user is a Department staff.', verbose_name='Department staff')),
                ('is_student', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active student. ', verbose_name='is student')),
                ('is_exco', models.BooleanField(default=False, help_text='Designates whether this user should be displayed in the excos page. ', verbose_name='Department exco')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
