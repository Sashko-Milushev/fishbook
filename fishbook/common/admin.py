from django.contrib import admin

from fishbook.common.models import PhotoComment


@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    pass
