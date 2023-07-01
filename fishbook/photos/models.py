from enum import Enum

from django.contrib.auth import get_user_model
from django.db import models

from fishbook.core.model_mixins import ChoicesEnumMixin
from fishbook.fish.models import Fish
from fishbook.photos.validators import validate_image
from cloudinary.models import CloudinaryField


UserModel = get_user_model()


class FishingStyle(ChoicesEnumMixin, Enum):
    float_fishing = 'Float fishing'
    feeder_fishing = 'Feeder fishing'
    fly_fishing = 'Fly fishing'
    carp_fishing = 'Carp fishing'
    spin_fishing = 'Spin fishing'
    ice_fishing = 'Ice fishing'
    trolling_fishing = 'Trolling fishing'
    salt_water_fishing = 'Salt water fishing'
    spear_fishing = 'Spear fishing'


class Photo(models.Model):
    MAX_DESCRIPTION_LENGTH = 50

    MAX_LOCATION_LENGTH = 30

    photo = CloudinaryField(
        folder='photos/',
        blank=False,
        null=False,
        validators=(
            validate_image,
        ),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        blank=True,
        null=True,
    )

    publication_date = models.DateField(
        auto_now=True,
        blank=True,
        null=False,
    )

    tagged_fish = models.ManyToManyField(
        Fish,
        blank=True,

    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )

    fishing_style = models.CharField(
        choices=FishingStyle.choices(),
        max_length=FishingStyle.max_len(),
        blank=True,
        null=True,
    )
