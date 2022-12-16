from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.exceptions import ValidationError
from django.forms import CheckboxSelectMultiple, PasswordInput, EmailInput

from fishbook.accounts.models import Profile

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2',)
        field_classes = {
            'email': auth_forms.UsernameField,
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget = EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter email'})
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

    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username')
        profile_type = self.cleaned_data.get('profile_type')
        profile_picture = self.cleaned_data.get('profile_picture')
        fishing_style = self.cleaned_data.get('fishing_style')
        message = 'Please fill the whole form.'
        if not username:
            self.add_error('username', message)
        if not profile_type:
            self.add_error('profile_type', message)
        if not profile_picture:
            self.add_error('profile_picture', message)
        if not fishing_style:
            self.add_error('fishing_style', message)


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass


class PasswordChangeForm(auth_forms.PasswordChangeForm):
    class Meta:
        model = UserModel
