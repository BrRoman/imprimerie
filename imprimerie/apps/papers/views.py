""" apps/papers/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Paper
from .forms import PaperForm


@login_required
def list(request):
    """ List of papers. """
    papers = Paper.objects.all().order_by('name', 'dim1', 'dim2')
    return render(
        request,
        'papers/list.html',
        {
            'papers': papers,
        },
    )


@login_required
def create(request):
    """ Create a paper. """
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('papers:list'))

    form = PaperForm()

    return render(
        request,
        'papers/form.html',
        {
            'form': form,
        }
    )


@login_required
def details(request, **kwargs):
    """ Details of a paper. """
    paper = Paper.objects.get(pk=kwargs['pk'])
    papers = Paper.objects.all().order_by('name', 'dim1', 'dim2')
    return render(
        request,
        'papers/details.html',
        {
            'paper': paper,
            'papers': papers,
        }
    )


@login_required
def update(request, **kwargs):
    """ Update a paper. """
    paper = Paper.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'papers:details',
                    kwargs={
                        'pk': paper.pk,
                    }
                )
            )

    else:
        form = PaperForm(instance=paper)

    return render(
        request,
        'papers/form.html',
        {
            'form': form,
            'paper': paper,
        }
    )


@login_required
def delete(request, **kwargs):
    """ Delete a paper. """
    paper = Paper.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = PaperForm(request.POST, instance=paper)
        paper.delete()
        return HttpResponseRedirect(reverse('papers:list'))

    form = PaperForm(instance=paper)

    return render(
        request,
        'papers/delete.html',
        {
            'form': form,
            'paper': paper,
        },
    )
