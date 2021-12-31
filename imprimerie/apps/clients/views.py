""" apps/clients/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Client
from .forms import ClientForm


@login_required
def list(request):
    """ List of clients. """
    clients = Client.objects.all()
    return render(
        request,
        'clients/list.html',
        {
            'clients': clients,
        },
    )


@login_required
def create(request):
    """ Create a client. """
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('clients:list'))

    form = ClientForm()

    return render(
        request,
        'clients/form.html',
        {
            'form': form,
        }
    )


@login_required
def details(request, **kwargs):
    """ Details of a client. """
    if 'pk' in kwargs.keys():
        client = Client.objects.get(pk=kwargs['pk'])
    else:
        client = Client.objects.all().order_by('-modified')[0]
        redirect('clients:details', pk=client.pk, permanent=True)
    clients = Client.objects.all().order_by('-modified')
    return render(
        request,
        'clients/details.html',
        {
            'client': client,
            'clients': clients,
        }
    )


@login_required
def update(request, **kwargs):
    """ Update a client. """
    client = Client.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'clients:details',
                    kwargs={
                        'pk': client.pk,
                    }
                )
            )

    else:
        form = ClientForm(instance=client)

    return render(
        request,
        'clients/form.html',
        {
            'form': form,
            'client': client,
        }
    )


@login_required
def delete(request, **kwargs):
    """ Delete a client. """
    client = Client.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        client.delete()
        return HttpResponseRedirect(reverse('clients:list'))

    form = ClientForm(instance=client)

    return render(
        request,
        'clients/delete.html',
        {
            'form': form,
            'client': client,
        },
    )
