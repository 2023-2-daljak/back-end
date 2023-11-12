from django.db import models
from common.models import Common
from common import models as core_models


class AbstractItem(core_models.Common):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Department(AbstractItem):

    """ RoomType Model Definition """

    class Meta:
        verbose_name = "학과"


class Species(AbstractItem):

    """ Amenity Model Definition """

    class Meta:
        verbose_name_plural = "종류"


class Grade(AbstractItem):

    """ Facility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "학년"


class Repair(AbstractItem):

    """ HouseRule Model Definition """

    class Meta:
        verbose_name = "보수"


class SearchHistory(models.Model):

    query = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="ss",  null=True, blank=False
    )
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.query


class Product(Common):

    SEMI_A = "it"
    SEMI_B = "마케팅"
    SEMI_C = "언어"
    SEMI_D = "제작/글쓰기"

    SEMI_CHOICES = (
        (SEMI_A, "it"),
        (SEMI_B, "마케팅"),
        (SEMI_C, "언어"),
        (SEMI_D, "제작/글쓰기"),
    )
    registrant = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True
    )

    filter = models.CharField(
        choices=SEMI_CHOICES, default='', max_length=10, blank=False, null=True)
    title = models.CharField(max_length=50, null=True,)
    content = models.TextField(
        null=True,
    )
    profile = models.ImageField(blank=True)
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

    # 필터

    department = models.ManyToManyField(
        "Department", related_name="department", blank=True)
    species = models.ManyToManyField(
        "Species", related_name="species", blank=True)
    grade = models.ManyToManyField("Grade", blank=True)
    repair = models.ManyToManyField("Repair", blank=True)

    @property
    def get_photo_url(self):
        if self.profile:
            return self.profile.url
        else:
            return "/static/images/user.jpg"

    def __str__(self):
        return f"{self.title} / by {self.registrant}"
