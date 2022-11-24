from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models
from multiselectfield import MultiSelectField

from fishbook.accounts.managers import AppUserManager
from fishbook.accounts.validators import validate_image
from fishbook.core.model_mixins import StrFromFieldMixin
from fishbook.fishing_styles.fishing_styles import FISHING_STYLES, FISHING_STYLES_MAX_LENGTH, FISHING_STYLES_MAX_CHOICES


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


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class ProfileType(ChoicesEnumMixin, Enum):
    fisherman = 'Fisherman'
    lake_owner = 'Lake owner'


class Profile(StrFromFieldMixin, models.Model):
    str_fields = ('profile_picture',)
    USERNAME_MAX_LENGTH = 30
    USERNAME_MIN_LENGTH = 2

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=False,
        null=False,
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
        blank=False,
        null=False,
    )

    fishing_style = MultiSelectField(
        choices=FISHING_STYLES,
        max_length=FISHING_STYLES_MAX_LENGTH,
        max_choices=FISHING_STYLES_MAX_CHOICES,
        blank=False,
        null=False,
    )

    profile_type = models.CharField(
        choices=ProfileType.choices(),
        max_length=ProfileType.max_len(),
        blank=False,
        null=False,
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )
