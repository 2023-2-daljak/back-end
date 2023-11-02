from django.db import models
from common.models import Common


class Product(Common):
    registrant = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50, null=True,)
    content = models.TextField(
        null=True,
    )

    image = models.ManyToManyField(
        # 이미지를 이미지필드로 할것이냐 manytomany로할것이냐=> 이미지 필드는 여개 선택인 안됨
        # => m:m으로 하자
        "photos.Photo",
        blank=True,

    )

    price = models.PositiveBigIntegerField(
        null=True,
    )

    categories = models.ForeignKey(   # 카테고리
        "product_categories.ProductCategory",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.title} / by {self.registrant}"
