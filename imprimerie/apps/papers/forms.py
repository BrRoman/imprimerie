""" apps/papers/forms.py """

from django import forms

from .models import Paper


class PaperForm(forms.ModelForm):
    """ Form for Paper. """
    name = forms.CharField(
        max_length=255,
        label='Nom',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
            }
        )
    )

    class Meta:
        model = Paper
        fields = [
            'name',
        ]
