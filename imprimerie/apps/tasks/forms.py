""" apps/tasks/forms.py """

from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    """ Form for Task. """
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
        model = Task
        fields = [
            'name',
        ]
