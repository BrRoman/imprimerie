""" apps/tasks/views.py """

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Task
from .forms import TaskForm


@login_required
def list(request):
    """ List of tasks. """
    tasks = Task.objects.all()
    return render(
        request,
        'tasks/list.html',
        {
            'tasks': tasks,
        },
    )


@login_required
def create(request):
    """ Create a task. """
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('tasks:list'))

    form = TaskForm()

    return render(
        request,
        'tasks/form.html',
        {
            'form': form,
        }
    )


@login_required
def details(request, **kwargs):
    """ Details of a task. """
    if 'pk' in kwargs.keys():
        task = Task.objects.get(pk=kwargs['pk'])
    else:
        task = Task.objects.all().order_by('-modified')[0]
        redirect('tasks:details', pk=task.pk, permanent=True)
    tasks = Task.objects.all().order_by('-modified')
    return render(
        request,
        'tasks/details.html',
        {
            'task': task,
            'tasks': tasks,
        }
    )


@login_required
def update(request, **kwargs):
    """ Update a task. """
    task = Task.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse(
                    'tasks:details',
                    kwargs={
                        'pk': task.pk,
                    }
                )
            )

    else:
        form = TaskForm(instance=task)

    return render(
        request,
        'tasks/form.html',
        {
            'form': form,
            'task': task,
        }
    )


@login_required
def delete(request, **kwargs):
    """ Delete a task. """
    task = Task.objects.get(pk=kwargs['pk'])
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        task.delete()
        return HttpResponseRedirect(reverse('tasks:list'))

    form = TaskForm(instance=task)

    return render(
        request,
        'tasks/delete.html',
        {
            'form': form,
            'task': task,
        },
    )
