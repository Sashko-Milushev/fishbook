from django import forms

from fishbook.fish.models import Fish


class AddFishForm(forms.ModelForm):
    class Meta:
        model = Fish
        exclude = ('caught_by',)

