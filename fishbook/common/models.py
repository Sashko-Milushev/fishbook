from django.contrib.auth import get_user_model
from django.db import models

from fishbook.photos.models import Photo

UserModel = get_user_model()


class PhotoLike(models.Model):
    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        blank=True,
        null=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )


class PhotoComment(models.Model):
    MAX_COMMENT_LENGTH = 50

    text = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        blank=False,
        null=False,
    )

    publication = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        blank=True,
        null=False
    )
