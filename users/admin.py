from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SocialUserCreationForm, SocialUserChangeForm
from .models import SocialUser


class SocialUserAdmin(UserAdmin):
    add_form = SocialUserCreationForm
    form = SocialUserChangeForm
    model = SocialUser
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        ('Main Info', {'fields': ('username', 'first_name', 'last_name', 'email', 'password')}),
        ('Profile', {'fields': ('profile_bio', 'profile_pic')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'id')
    ordering = ('id',)


admin.site.register(SocialUser, SocialUserAdmin)
