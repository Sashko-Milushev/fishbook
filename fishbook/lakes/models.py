from django.contrib.auth import get_user_model
from django.db import models

from fishbook.fish.models import Fish

from cloudinary.models import CloudinaryField

UserModel = get_user_model()


class PublicLake(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_REGION_LENGTH = 30
    MAX_LINK_LENGTH = 300
    MAX_ADDRESS_LENGTH = 100

    name = models.CharField(
        verbose_name='Lake Name',
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )
    photo = CloudinaryField(
        verbose_name='Lake Photo',
        folder='lake_pictures/',
        blank=False,
        null=True,
    )
    fish = models.ManyToManyField(
        Fish,
        verbose_name='Fish',
        blank=False,

    )
    region = models.CharField(
        verbose_name='Region',
        max_length=MAX_REGION_LENGTH,
        blank=False,
        null=False,
    )
    address = models.CharField(
        verbose_name='Address',
        max_length=MAX_ADDRESS_LENGTH,
        blank=True,
        null=True,
    )
    google_maps_link = models.CharField(
        verbose_name='Google Link',
        max_length=MAX_LINK_LENGTH,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'Lake {self.name}'


class PrivateLake(models.Model):
    MAX_TAX_DIGITS = 5
    TAX_DECIMAL_PLACES = 2
    MAX_PHONE_LENGTH = 25
    MAX_NAME_LENGTH = 30
    MAX_REGION_LENGTH = 30
    MAX_LINK_LENGTH = 300
    MAX_ADDRESS_LENGTH = 100

    name = models.CharField(
        verbose_name='Lake Name',
        max_length=MAX_NAME_LENGTH,
        blank=False,
        null=False,
    )
    photo = CloudinaryField(
        verbose_name='Lake Photo',
        folder='lake_pictures/',
        blank=False,
        null=True,

    )
    fish = models.ManyToManyField(
        Fish,
        verbose_name='Fish',
        blank=False,

    )
    region = models.CharField(
        verbose_name='Region',
        max_length=MAX_REGION_LENGTH,
        blank=False,
        null=False,
    )
    address = models.CharField(
        verbose_name='Address',
        max_length=MAX_ADDRESS_LENGTH,
        blank=True,
        null=True,
    )
    google_maps_link = models.CharField(
        verbose_name='Google Link',
        max_length=MAX_LINK_LENGTH,
        blank=True,
        null=True
    )

    owner = models.ForeignKey(
        UserModel,
        verbose_name='Lake Owner',
        on_delete=models.CASCADE,

    )
    phone = models.CharField(
        verbose_name='Phone',
        max_length=MAX_PHONE_LENGTH,
        blank=True,
        null=True,
    )
    day_tax = models.DecimalField(
        max_digits=MAX_TAX_DIGITS,
        decimal_places=TAX_DECIMAL_PLACES,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f'Lake {self.name}'
