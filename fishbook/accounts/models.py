from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from fishbook.accounts.managers import AppUserManager
from fishbook.accounts.validators import validate_image
from fishbook.core.model_mixins import StrFromFieldMixin, ChoicesEnumMixin


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )

    is_staff = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()


class ProfileType(ChoicesEnumMixin, Enum):
    fisherman = 'Fisherman'
    lake_owner = 'Lake owner'


class FavouriteFishingStyle(ChoicesEnumMixin, Enum):
    float_fishing = 'Float fishing'
    feeder_fishing = 'Feeder fishing'
    fly_fishing = 'Fly fishing'
    carp_fishing = 'Carp fishing'
    spin_fishing = 'Spin fishing'
    ice_fishing = 'Ice fishing'
    trolling_fishing = 'Trolling fishing'
    salt_water_fishing = 'Salt water fishing'
    spear_fishing = 'Spear fishing'


class Profile(StrFromFieldMixin, models.Model):
    str_fields = ('profile_picture',)
    USERNAME_MAX_LENGTH = 30
    USERNAME_MIN_LENGTH = 2

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        validators=(
            validate_image,
        ),
    )

    username = models.CharField(
        unique=True,
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(USERNAME_MIN_LENGTH),
        ),
        blank=True,
        null=True,
    )

    fishing_style = models.CharField(
        choices=FavouriteFishingStyle.choices(),
        max_length=FavouriteFishingStyle.max_len(),
        blank=True,
        null=True,
    )

    profile_type = models.CharField(
        choices=ProfileType.choices(),
        max_length=ProfileType.max_len(),
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
    is_completed = models.BooleanField(
        default=False,
        blank=True,
        null=True,
    )

