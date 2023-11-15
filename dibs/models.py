from django.db import models
from common.models import Common


class Dib(Common):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    
    
    products = models.ForeignKey(
        "products.Product",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return f"{self.owner}'s dib"
