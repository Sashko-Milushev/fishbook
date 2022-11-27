from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from fishbook.accounts.models import Profile
from fishbook.fishing_styles.fishing_styles import FISHING_STYLES

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        # TODO: check if 'field_classes' is correct
        field_classes = {'email': auth_forms.UsernameField}


class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        field_classes = {'email': auth_forms.UsernameField}


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'profile_type', 'profile_picture', 'fishing_style')
        widgets = forms.CheckboxSelectMultiple, choices = FISHING_STYLES


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    pass
