from django import forms

from fishbook.lakes.models import PrivateLake


class PrivateLakeBaseForm(forms.ModelForm):
    class Meta:
        model = PrivateLake
        fields = ('name', 'photo', 'fish', 'region', 'address', 'google_maps_link', 'phone', 'day_tax')


class PrivateLakeCreationForm(PrivateLakeBaseForm):
    pass


class PrivateLakeEditForm(PrivateLakeBaseForm):
    pass


class PrivateLakeDeleteForm(PrivateLakeBaseForm):
    pass
