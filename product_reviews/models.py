from django.db import models
from common.models import Common


class ProductReview(Common):
    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
    )
    
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        null=True,
    )
    
    title = models.CharField(max_length=50,
                             null=True,)
    content = models.TextField(
        null=True,
    )
    
    rating = models.PositiveIntegerField(
        null=True,
    )
    
    def __str__(self):
        return f"{self.writer} : {self.rating}⭐️"