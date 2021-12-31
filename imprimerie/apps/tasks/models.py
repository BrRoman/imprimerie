""" apps/tasks/models.py """

from django.db import models
from django.db.models.deletion import CASCADE

from apps.clients.models import Client
from apps.papers.models import Paper


class Task(models.Model):
    """ Task model. """
    client = models.ForeignKey(
        Client,
        on_delete=CASCADE,
    )
    name = models.CharField(
        max_length=255,
    )
    paper = models.ForeignKey(
        Paper,
        on_delete=CASCADE,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
