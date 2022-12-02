from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.forms import CheckboxSelectMultiple

from fishbook.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        # TODO: check if 'field_classes' is correct
        # field_classes = {'email': auth_forms.UsernameField}


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        field_classes = {'email': auth_forms.UsernameField}


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'profile_type', 'profile_picture', 'fishing_style',)


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = UserModel
