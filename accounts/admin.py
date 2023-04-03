from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from .models import *
from django.contrib.auth.models import Group


# ----------------------------- User ---------------------------------------
@register(User)
class UserAdmin(AbstractUserAdmin):
    
    list_display = ('first_name', 'last_name', 'phone', 'email', 'username', \
                    'valid_phone', 'valid_email', 'get_date_joined',\
                    'is_active', 'is_staff', 'is_superuser'
    )

    list_filter = ('is_active', 'is_superuser', 'valid_phone', 'valid_email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    readonly_fields = ('get_date_joined', 'get_last_update', 'get_last_login')
    list_display_links = ('first_name', 'last_name')
    ordering = ('-is_superuser', '-is_staff', '-date_joined')

    fieldsets = (
        ('اطلاعات ورود', {
            'fields': ('username', 'password')
        }),

        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'gender', 'phone', 'email')
        }),

        ('احراز هویت‌ها', {
            'fields': ('valid_phone', 'valid_email')
        }),

        ('دسترسی‌ها', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'user_permissions',
            )
        }),

        ('تاریخ‌های مهم', {
            'fields': ('get_date_joined', 'get_last_update', 'get_last_login')
        })
    )

    add_fieldsets = (
        ('اطلاعات ورود', {
            'fields': ('username', 'password1', 'password2')
        }),

        ('اطلاعات شخصی', {
            'fields': ('first_name', 'last_name', 'gender', 'phone', 'email')
        }),

        ('دسترسی‌ها', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'user_permissions',
            )
        })
    )