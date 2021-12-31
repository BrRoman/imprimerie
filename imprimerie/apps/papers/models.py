""" apps/papers/models.py """

from django.db import models


class Paper(models.Model):
    """ Task Model. """
    name = models.CharField(
        max_length=255,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
    )
    length = models.CharField(
        max_length=7,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name
