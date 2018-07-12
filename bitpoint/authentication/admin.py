# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from bitpoint.authentication.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with ID Number field."""
    fieldsets = (
        (None, {'fields': ('ID_Number', 'password')}),
        (_('Details'), {'fields': 
            (
                'first_name', 
                'last_name',
                'gender',
                )
            }),

        (_('Permissions'), {'fields': 
            (
                'is_active', 
                'is_d_staff',
                'is_exco',
                'is_staff', 
                'is_superuser',
                'groups', 
                'user_permissions'
                )
            }),


        (_('Social Networks'), {'fields':
         (
            'facebook_id',
            'twitter_handler',
            'instagram_id',
            'pinterest',
            )
         }),

       (_('Contact Details'), {'fields':
         (
            'mobile',
            'email',
            'hall_of_residence',
            'state_of_origin',
            'town',
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

    list_display = ('ID_Number', 'first_name', 'last_name', 'level', 'mobile', 'hall_of_residence', 'state_of_origin', 'is_active', 'is_d_staff', 'is_exco')
    list_filter = ('hall_of_residence', 'state_of_origin', 'is_d_staff', 'is_exco', 'is_active')
    list_per_page = 50
    ordering = ('first_name',)
    readonly_fields = ('ID_Number',)

admin.site.site_header = "NAITS - Online Voting"
admin.site.site_title = "NAITS - Mautech"
admin.site.index_title = "NAIT Election Commitee | Administration"