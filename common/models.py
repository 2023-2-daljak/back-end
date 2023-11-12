from django.db import models
from . import managers

""" Commom Model Definition"""


class Common(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True