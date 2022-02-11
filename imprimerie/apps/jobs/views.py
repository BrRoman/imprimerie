""" apps/jobs/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from apps.elements.models import Element
from .models import Job
from .forms import JobForm


@login_required
def list(request):
    """ List of jobs. """
    jobs = Job.objects.all().order_by('created')
    return render(
        request,
        'jobs/list.html',
        {
            'jobs': jobs,
        },
    )


@login_required
def create(request):
    """ Create a job. """
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('jobs:list'))

    form = JobForm()

    return render(
        request,
        'jobs/form.html',
        {
            'form': form,
        }
    )


@login_required
def details(request, **kwargs):
    """ Details of a job. """
    job = Job.objects.get(pk=kwargs['pk'])
    elements = Element.objects.filter(job=job)
    return render(
        request,
        'jobs/details.html',
        {
            'job': job,
            'elements': elements,
        }
    )


@login_required
def update(request, **kwargs):
    """ Update a job. """
    job = Job.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'jobs:details',
                    kwargs={
                        'pk': job.pk,
                    }
                )
            )

    else:
        form = JobForm(instance=job)

    return render(
        request,
        'jobs/form.html',
        {
            'form': form,
            'job': job,
        }
    )


@login_required
def delete(request, **kwargs):
    """ Delete a job. """
    job = Job.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        job.delete()
        return HttpResponseRedirect(reverse('jobs:list'))

    form = JobForm(instance=job)

    return render(
        request,
        'jobs/delete.html',
        {
            'form': form,
            'job': job,
        },
    )
