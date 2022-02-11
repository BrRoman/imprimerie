""" apps/elements/models.py """

from django.db import models
from django.db.models.deletion import CASCADE

from apps.jobs.models import Job
from apps.papers.models import Paper


class Element(models.Model):
    """ Element model. """
    job = models.ForeignKey(
        Job,
        on_delete=CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=255,
    )
    quantity = models.IntegerField()
    color = models.CharField(
        max_length=255,
        choices=[
            ('quadri', 'quadri'),
            ('black', 'black'),
        ],
    )
    paper = models.ForeignKey(
        Paper,
        on_delete=CASCADE,
    )
    paper_cut_into = models.IntegerField()
    paper_dim1_machine = models.FloatField()
    paper_dim2_machine = models.FloatField()
    file_width = models.FloatField()
    file_height = models.FloatField()
    imposition = models.IntegerField()
    number_of_pages = models.IntegerField()
    recto_verso = models.BooleanField()
    observations = models.TextField()

    def __str__(self):
        return self.name
