from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class UserKindChoices(models.TextChoices):
        CLIENT = ("client", "Client")  # 외주하는 사람들
        STUDENT = ("student", "Student")  # 수정 => 대학생들

    avatar = models.ImageField(
        blank=True,
    )
    password = models.CharField(
        max_length=200,
    )
    email = models.CharField(
        max_length=150,
    )
    birth = models.CharField(
        max_length=8,
    )
    nickname = models.CharField(
        max_length=100,
    )
    gender = models.CharField(
        max_length=6,
        choices=GenderChoices.choices,
    )
    phone_num = models.PositiveBigIntegerField(null=True, blank=True)
    user_kind = models.CharField(
        max_length=10,
        choices=UserKindChoices.choices,
    )
    location = models.CharField(
        max_length=100,
    )
    
    def __str__(self):
        return self.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 좋아요를 누른 사용자
    item_id = models.CharField(max_length=100)  # 좋아요한 항목의 ID (예: project1)
    # 좋아요 상태 (True: 좋아요, False: 좋아요 취소)
    is_liked = models.BooleanField(default=True)
