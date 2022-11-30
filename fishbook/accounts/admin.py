from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from fishbook.accounts.forms import SignUpForm, UserEditForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('id',)
    list_display = ['id', 'email', 'last_login', ]
    list_filter = ()
    form = UserEditForm
    add_form = SignUpForm
    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {'fields': (
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',),
        },
         ),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
