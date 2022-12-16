from django.contrib.auth import get_user_model

from fishbook.accounts.models import Profile

UserModel = get_user_model()


def get_user_by_id(pk):
    return UserModel.objects.filter(pk=pk).get()


def get_profile_by_id(pk):
    return Profile.objects.filter(pk=pk).get()
