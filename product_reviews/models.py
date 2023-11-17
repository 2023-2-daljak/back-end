from django.db import models
from common.models import Common


class ProductReview(Common):
    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        related_name="reviews",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        null=True,
        related_name="reviews",
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

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."

    class Meta:
        ordering = ("-created_at",)
