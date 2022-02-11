""" apps/elements/forms.py """

from django import forms

from apps.papers.models import Paper
from .models import Element


class ElementForm(forms.ModelForm):
    """ Form for Element. """
    name = forms.CharField(
        max_length=255,
        label='Nom',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
            }
        ),
    )
    quantity = forms.IntegerField(
    )
    paper = forms.ModelChoiceField(
        queryset=Paper.objects.all().order_by('name'),
    )
    paper_cut_into = forms.IntegerField(
    )
    paper_dim1_machine = forms.FloatField()
    paper_dim2_machine = forms.FloatField()
    file_width = forms.FloatField()
    file_height = forms.FloatField()
    imposition = forms.IntegerField()
    number_of_pages = forms.IntegerField()
    recto_verso = forms.BooleanField()

    class Meta:
        model = Element
        fields = [
            'name',
            'quantity',
            'paper',
            'paper_cut_into',
            'paper_dim1_machine',
            'paper_dim2_machine',
            'file_width',
            'file_height',
            'imposition',
            'number_of_pages',
            'recto_verso',
        ]
