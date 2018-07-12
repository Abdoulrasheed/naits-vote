#-*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Aspirant, Office, Voter
from bitpoint.authentication.models import User as Student
from django.contrib.auth.models import Group


class AspirantInline(admin.TabularInline):
    model = Aspirant
    readonly_fields = ('votes',)
    extra = 3


class OfficeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['office'],
        }),
    ]
    inlines = [AspirantInline]
    list_display = ('office',)
    search_fields = ('office',)

class VoterAdmin(admin.ModelAdmin):
    fieldsets = [
    ('Student',{
        'fields': ['student', 'office']
        })

    ]
    readonly_fields = ('student', 'office')
    list_display = ('student', 'office')

class AspirantAdmin(admin.ModelAdmin):
    list_display = ('names', 'level', 'aspiring_for', 'votes')
    list_filter = ('level', 'aspiring_for')
    list_per_page = 10
    ordering = ('-level','-votes')
    readonly_fields = ('votes',)

    
    def names(self, obj):
        return obj.first_name + " " + obj.last_name


admin.site.register(Office, OfficeAdmin)
admin.site.register(Aspirant, AspirantAdmin)
admin.site.register(Voter, VoterAdmin)