""" apps/main/models.py """

from django.db import models


class Work(models.Model):
    """ Work Model. """
    name = models.CharField(
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
