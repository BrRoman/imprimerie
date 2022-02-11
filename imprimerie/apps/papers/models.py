""" apps/papers/models.py """

from django.db import models


class Paper(models.Model):
    """ Element Model. """
    name = models.CharField(
        max_length=255,
    )
    dim1 = models.CharField(
        max_length=3,
    )
    dim2 = models.CharField(
        max_length=3,
    )
    weight = models.IntegerField()
    price = models.DecimalField(
        decimal_places=2,
        max_digits=7,
    )

    def __str__(self):
        return '{} {}g {}x{}'.format(self.name, self.weight, self.dim1, self.dim2)
