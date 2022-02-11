""" apps/jobs/models.py """

from django.db import models
from django.db.models.deletion import CASCADE

from apps.clients.models import Client


class Job(models.Model):
    """ Job model. """
    name = models.CharField(
        max_length=255,
    )
    client = models.ForeignKey(
        Client,
        on_delete=CASCADE,
    )
    quantity_client = models.IntegerField()
    finition = models.CharField(
        max_length=255,
    )
    dim1_finished = models.IntegerField()
    dim2_finished = models.IntegerField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
