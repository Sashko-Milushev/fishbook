from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple, PasswordInput

from fishbook.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2',)
        field_classes = {
            'email': auth_forms.UsernameField,
        }
        widgets = {
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter password'})
        self.fields['password2'].widget = PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Repeat password'})


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        field_classes = {
            'email': auth_forms.UsernameField,
        }


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
