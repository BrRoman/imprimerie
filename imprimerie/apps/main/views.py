""" apps/main/views.py """

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Work
from .forms import WorkForm


def list(request):
    """ List of works. """
    works = Work.objects.all().order_by('-modified')
    return render(
        request,
        'main/list.html',
        {
            'works': works,
        },
    )

def details(request, **kwargs):
    """ Details of a work. """
    work = Work.objects.get(pk=kwargs['pk'])
    return render(
        request,
        'main/details.html',
        {
            'work': work,
        }
    )

def update(request, **kwargs):
    """ Update a work. """
    work = Work.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'main:details',
                    kwargs={
                        'pk': work.pk,
                    }
                )
            )

    else:
        form = WorkForm(instance=work)

    return render(
        request,
        'main/form.html',
        {
            'form': form,
            'work': work,
        }
    )
