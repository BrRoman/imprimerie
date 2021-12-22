""" apps/main/views.py """

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    """ Home page of the Imprimerie. """
    return render(
        request,
        'main/home.html',
        {},
    )
