""" apps/elements/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.jobs.models import Job
from .models import Element
from .forms import ElementForm


@login_required
def create(request, **kwargs):
    """ Create a element. """
    job = Job.objects.get(pk=kwargs['job'])
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid:
            element = form.save(commit=False)
            element.job = job
            element.save()
            return HttpResponseRedirect(
                reverse(
                    'jobs:details',
                    kwargs={'pk': job.pk},
                )
            )

    form = ElementForm()

    return render(
        request,
        'elements/form.html',
        {
            'form': form,
            'job': job,
        }
    )


@login_required
def details(request, **kwargs):
    """ Details of a element. """
    element = Element.objects.get(pk=kwargs['pk'])
    job = element.job
    price_sheet = element.paper.price / element.paper_cut_into / 1000
    return render(
        request,
        'elements/details.html',
        {
            'element': element,
            'job': job,
            'price_sheet': price_sheet,
        }
    )


@login_required
def update(request, **kwargs):
    """ Update an element. """
    element = Element.objects.get(pk=kwargs['pk'])
    job = element.job
    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)
        if form.is_valid():
            element = form.save(commit=False)
            element.job = job
            element.save()
            return HttpResponseRedirect(
                reverse(
                    'jobs:details',
                    kwargs={'pk': job.pk},
                )
            )

    else:
        form = ElementForm(instance=element)

    return render(
        request,
        'elements/form.html',
        {
            'form': form,
            'element': element,
            'job': job,
        }
    )


@login_required
def delete(request, **kwargs):
    """ Delete a element. """
    element = Element.objects.get(pk=kwargs['pk'])
    job = element.job
    if request.method == 'POST':
        form = ElementForm(request.POST, instance=element)
        element.delete()
        return HttpResponseRedirect(reverse('jobs:details', kwargs={'pk': job.pk}))

    form = ElementForm(instance=element)

    return render(
        request,
        'elements/delete.html',
        {
            'form': form,
            'element': element,
            'job': job,
        },
    )
