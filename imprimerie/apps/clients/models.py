""" apps/clients/models.py """

from django.db import models


class Client(models.Model):
    """ Client model. """
    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,
    )
    address1 = models.CharField(
        max_length=255,
    )
    address2 = models.CharField(
        max_length=255,
    )
    address3 = models.CharField(
        max_length=255,
    )
    zip = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.first_name + \
            (' ' if self.first_name and self.last_name else '') + \
            self.last_name
