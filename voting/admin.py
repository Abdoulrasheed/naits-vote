#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Aspirant, Office, Voter


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
    search_fields = ['office']

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
    def names(self, obj):
        return obj.first_name + " " + obj.last_name

admin.site.site_header = "NAITS - Online Voting"
admin.site.site_title = "IT Innovators Group - Mautech"
admin.site.index_title = "NAIT Election Commitee - Administration"

admin.site.register(Office, OfficeAdmin)
admin.site.register(Aspirant, AspirantAdmin)
admin.site.register(Voter, VoterAdmin)
