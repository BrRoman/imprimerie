""" apps/accounts/views.py """

from django.contrib.auth.views import LoginView

from .forms import ImprimerieLoginForm


class ImprimerieLoginView(LoginView):
    """ Login view. """
    form_class = ImprimerieLoginForm
    template_name = 'accounts/login.html'
