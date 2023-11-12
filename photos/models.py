from django.db import models
from common.models import Common


class Photo(Common):
    photo_title = models.CharField(max_length=50,null=True,)
    file = models.FileField()

    def __str__(self):
        return f"{self.photo_title}"