""" Django models utilities"""
from django.db import models

class CRideModel(models.Model):
    """
    Comparte Rise base model.

    CRideModel acts an abstract base class from each every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the objects was created
        + modified (DateTime): Store the last datetime the objects was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the objects was created.'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the objects was last modified.'
    )

    class Meta:
        """Meta option."""
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']