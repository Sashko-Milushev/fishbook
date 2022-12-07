from enum import Enum

from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models

from fishbook.core.model_mixins import StrFromFieldMixin, ChoicesEnumMixin

UserModel = get_user_model()


class FishType(ChoicesEnumMixin, Enum):
    predatory = 'Predatory'
    peaceful = 'Peaceful'


class Fish(StrFromFieldMixin, models.Model):
    str_fields = ('id', 'name')
    MAX_LENGTH_NAME = 30
    MIN_LENGTH_NAME = 2

    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 1300

    name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        blank=False,
        null=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGTH_NAME),
        )
    )

    type = models.CharField(
        choices=FishType.choices(),
        max_length=FishType.max_len(),
        blank=False,
        null=False,
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        blank=True,
        null=True,
    )

    fish_picture = models.URLField(
        blank=False,
        null=False,
    )

    caught_by = models.ManyToManyField(
        UserModel,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Fish'
        ordering = ('name',)
