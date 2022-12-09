from django import forms

from fishbook.common.models import PhotoLike, PhotoComment
from fishbook.core.form_mixins import DisableFieldFormMixin
from fishbook.photos.models import Photo


class PhotoBaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('user', 'publication_date')


class PhotoCreateForm(PhotoBaseForm):
    pass


class PhotoEditForm(PhotoBaseForm):
    class Meta:
        model = Photo
        exclude = ('publication_date', 'photo', 'user',)


class PhotoDeleteForm(DisableFieldFormMixin, PhotoBaseForm):
    disabled_fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if commit:
            self.instance.tagged_fish.clear()
            Photo.objects.all().first().tagged_fish.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()

        return self.instance
