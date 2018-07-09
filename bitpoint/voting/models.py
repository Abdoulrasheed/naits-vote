#-*- coding: utf-8 -*-
import os.path
from django.db import models
from bitpoint.authentication.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

from local.constants import (STATES, 
                                LEVEL, 
                                EXCO_OFFICES, 
                                HALL_OF_RESIDENCE)


class Exco(models.Model):
    name = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
        )

    office = models.CharField(
        choices=EXCO_OFFICES, 
        blank=True, 
        null=True, 
        max_length=50
        )

    from_date = models.DateField(
        auto_now_add=True
        )

    to_date = models.DateField(
        auto_now_add=True
        )



class Office(models.Model):
    office = models.CharField(max_length=200)

    def __str__(self):  # Python 3: def __str__(self):
        return self.office



class Aspirant(models.Model):
    aspiring_for = models.ForeignKey(
        Office, 
        on_delete=models.CASCADE
        )

    first_name = models.CharField(
        max_length=200
        )

    last_name = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
        )

    nick_name = models.CharField(
        max_length=50, 
        blank=True, 
        null=True
        )

    level = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)


    def __str__(self):  # Python 3: def __str__(self):
        return self.first_name + " " + str(self.last_name)


class Voter(models.Model):
    student = models.ForeignKey(User)
    office = models.ForeignKey(Office)


    def __str__(self):
    
        if self.student.first_name and self.student.last_name:
            return str(self.student) + \
            " (" + self.student.first_name + " " + self.student.last_name + ")"
    
        else:
            return str(self.student)