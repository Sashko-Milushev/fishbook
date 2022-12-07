from django.contrib import admin

from fishbook.photos.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'publication_date', 'tagged_fish')

    @staticmethod
    def tagged_fish(current_photo_obj):
        fish_on_photo = current_photo_obj.tagged_fish.all()
        if fish_on_photo:
            return ', '.join(f.name for f in fish_on_photo)
        return 'No tagged fish'
