from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class UserKindChoices(models.TextChoices):
        CLIENT = ("client", "Client")  # 외주하는 사람들
        STUDENT = ("student", "Student") #수정 => 대학생들

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
    
    
