from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from . import models

class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'phone'),
        }),
        (_('Personal info'), {
            'fields': ('first_name', 'last_name', 'cart', 'address'),
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'verified_email', 'is_staff', 'is_superuser', 
                                       'groups', 'user_permissions'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined'),
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'phone', 'password1', 'password2'),
        }),
    )

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(models.User, UserAdmin)

admin.site.register(models.Address)