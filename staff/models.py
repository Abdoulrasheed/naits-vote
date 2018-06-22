# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from voting.models import User, STATES

POSITION = (
        ('Lecturer', 'Lecturer'),
        ('HOD', 'Head of Department'),
        ('Staff Advisor', 'Staff Advisor')

    )

class ListOfStaff(models.Model):
    name = models.ForeignKey(User, max_length=50,)
    position = models.CharField(choices=POSITION, max_length=50)
    state = models.CharField(max_length=50, choices=STATES, blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='staffs_profile_pictures/', blank=True, null=True)

