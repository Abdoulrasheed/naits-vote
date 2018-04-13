#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Office(models.Model):
    office = models.CharField(max_length=200)

    def __str__(self):  # Python 3: def __str__(self):
        return self.office

class Aspirant(models.Model):
    aspiring_for = models.ForeignKey(Office)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    nick_name = models.CharField(max_length=50, blank=True, null=True)
    level = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)


    def __str__(self):  # Python 3: def __str__(self):
        return self.first_name + " " + str(self.last_name)


class Voter(models.Model):
	student = models.ForeignKey(User)
	office = models.ForeignKey(Office)

	def __str__(self):
		return self.student.first_name + " " + self.student.last_name
