from django import forms

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
        exclude = ('publication_date', 'photo')
