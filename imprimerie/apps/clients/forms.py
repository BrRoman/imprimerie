""" apps/clients/forms.py """

from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    """ Form for Client. """
    first_name = forms.CharField(
        max_length=255,
        label='Prénom',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
            }
        )
    )
    last_name = forms.CharField(
        required=False,
        max_length=255,
        label='Nom',
        label_suffix='',
    )

    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
        ]
