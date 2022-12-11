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


class PhotoDeleteForm(PhotoBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].disabled = True
        self.fields['photo'].disabled = True
        self.fields['location'].disabled = True
        self.fields['tagged_fish'].disabled = True
        self.fields['fishing_style'].disabled = True

    def save(self, commit=True):
        if commit:
            self.instance.tagged_fish.clear()
            Photo.objects.all().first().tagged_fish.clear()
            PhotoLike.objects.filter(photo_id=self.instance.id).delete()
            PhotoComment.objects.filter(photo_id=self.instance.id).delete()
            self.instance.delete()

        return self.instance
