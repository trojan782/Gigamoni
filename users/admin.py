from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from django.db import models
from .models import GigaUser

#Register your models here.
class GigaUserAdminConfig(UserAdmin):
    model = GigaUser
    search_fields = ('email', 'full_name', 'phone_number')
    ordering = ('email'),
    list_display = ('email', 'full_name', 'phone_number', 'is_active', 'is_staff')

    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})}
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'phone_number', 'password1', 'password2', 'is_staff')}),
    )

admin.site.register(GigaUser, GigaUserAdminConfig)