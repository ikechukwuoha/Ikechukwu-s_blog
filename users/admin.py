from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from.forms import RegistrationForm, UpdateForm

from .models import MyUser, Profile



class CustomAdmin(UserAdmin):
    add_form = RegistrationForm
    form = UpdateForm
    model = MyUser
    
    search_fields = ('email', 'username')
    list_filter = ('email', 'username', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'username')}),
        ('permissions', {'fields': ('is_active', 'is_staff', 'is_admin')}),
        ('personal', {'fields': ()}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'is_active', 'is_staff', 'is_admin', 'password1', 'password2')},
        ),
    )



    
    

admin.site.register(Profile)
admin.site.register(MyUser, CustomAdmin)