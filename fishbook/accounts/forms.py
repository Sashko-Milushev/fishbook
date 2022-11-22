from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class SignUpForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        # TODO: check if 'field_classes' is correct
        field_classes = {'email': auth_forms.UsernameField}



