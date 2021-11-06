""" apps/main/forms.py """

from django import forms

from .models import Work

class WorkForm(forms.ModelForm):
    """ Form for Work. """
    name = forms.CharField(
        max_length=255,
        label='Nom',
        label_suffix='',
    )

    class Meta:
        model = Work
        fields = [
            'name',
        ]