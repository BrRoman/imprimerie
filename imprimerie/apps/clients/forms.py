""" apps/clients/forms.py """

from django import forms

from .models import Client


class ClientForm(forms.ModelForm):
    """ Form for Client. """
    quality = forms.ChoiceField(
        required=False,
        choices=[
            ('', ''),
            ('Monsieur', 'Monsieur'),
            ('Madame', 'Madame'),
            ('M. l\'Abbé', 'M. l\'Abbé'),
        ],
    )
    first_name = forms.CharField(
        required=False,
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
    address1 = forms.CharField(
        required=False,
        max_length=255,
    )
    address2 = forms.CharField(
        required=False,
        max_length=255,
    )
    address3 = forms.CharField(
        required=False,
        max_length=255,
    )
    zip = forms.CharField(
        required=False,
        max_length=255,
    )
    city = forms.CharField(
        required=False,
        max_length=255,
    )

    class Meta:
        model = Client
        fields = [
            'quality',
            'first_name',
            'last_name',
            'address1',
            'address2',
            'address3',
            'zip',
            'city',
        ]
