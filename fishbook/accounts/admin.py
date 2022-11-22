from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from fishbook.accounts.forms import SignUpForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'last_login']
    list_filter = ()
    add_form = SignUpForm
