#-*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import Aspirant, Office, Voter
from authentication.models import User as Student
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
    readonly_fields = ('votes',)
    def names(self, obj):
        return obj.first_name + " " + obj.last_name

class StateAdmin(object):
    """docstring for StateOfOriginAdmin"""
    def __init__(self, arg):
        super(StateOfOriginAdmin, self).__init__()
        self.arg = arg


@admin.register(Student)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with ID Number field."""
    fieldsets = (
        (None, {'fields': ('ID_Number', 'password')}),
        (_('Bio-Data'), {'fields': 
            (
                'first_name', 
                'last_name',
                )
            }),

        (_('Permissions'), {'fields': 
            (
                'is_active', 
                'is_staff', 
                'is_superuser',
                'groups', 
                'user_permissions'
                )
            }),

        (_('Important dates'), {'fields':
         (
            'last_login',
            )
         }),
        )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('ID_Number', 'password1', 'password2', 'level'),
            }),
        )

    list_display = ('ID_Number', 'first_name', 'last_name','is_staff',)
    search_fields = ('ID_Number', 'first_name', 'last_name')
    ordering = ('ID_Number',)

admin.site.site_header = "NAITS - Online Voting"
admin.site.site_title = "IT Innovators Group - Mautech"
admin.site.index_title = "NAIT Election Commitee | Administration"

admin.site.register(Office, OfficeAdmin)
admin.site.register(Aspirant, AspirantAdmin)
admin.site.register(Voter, VoterAdmin)