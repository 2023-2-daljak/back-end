from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import uuid
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


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

    major = models.CharField(max_length=20, blank=True,
                             null=True, verbose_name='전공')

    grade = models.IntegerField(
        max_length=1, blank=True, null=True, verbose_name="학년")

    phone_number = models.IntegerField(
        max_length=40, blank=True, null=True, verbose_name='전화번호')
    student_id = models.IntegerField(
        max_length=20, blank=True, null=True, verbose_name='학번')
    # 전공
    email_confirmed = models.BooleanField(default=False, verbose_name='이메일인증')
    email_secret = models.CharField(
        max_length=120, default="", blank=True, verbose_name='유저이름')

    def verify_email(self):
        if self.email_confirmed is False:
            secret = uuid.uuid4().hex[:30]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail("안녕하세요 daljk입니ㅏㄷ",
                      strip_tags(html_message),
                      "dongyu1472@gmail.com",
                      [self.email],
                      html_message=html_message,
                      )

            self.save()
        return


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 좋아요를 누른 사용자
    item_id = models.CharField(max_length=100)  # 좋아요한 항목의 ID (예: project1)
    # 좋아요 상태 (True: 좋아요, False: 좋아요 취소)
    is_liked = models.BooleanField(default=True)
