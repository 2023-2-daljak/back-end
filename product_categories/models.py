from django.db import models
from common.models import Common


class ProductCategory(Common):
    
    name = models.CharField(
        max_length=50,
    )
    
    def __str__(self):
        return f"{self.name}"
