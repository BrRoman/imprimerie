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
    dim1 = forms.CharField()
    dim2 = forms.CharField()
    weight = forms.IntegerField(
        required=False,
    )
    price = forms.DecimalField(
        required=False,
        decimal_places=2,
        max_digits=7,
    )

    class Meta:
        model = Paper
        fields = [
            'name',
            'dim1',
            'dim2',
            'weight',
            'price',
        ]
