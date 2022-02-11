""" apps/jobs/forms.py """

from django import forms

from apps.jobs.models import Client
from .models import Job


class JobForm(forms.ModelForm):
    """ Form for Job. """
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
    client = forms.ModelChoiceField(
        queryset=Client.objects.all().order_by('last_name', 'first_name'),
    )

    class Meta:
        model = Job
        fields = [
            'name',
            'client',
        ]
