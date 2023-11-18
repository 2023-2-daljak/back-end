from django import forms
from . import models
import django.contrib.auth.forms as auth_forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error(
                    "password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError(
                "User does not exist"))


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="패스워드확인")

    class Meta:
        model = models.User
        fields = ("username","email", "password",  )
        
    widget = {
            "username": forms.TextInput(attrs={'placeholder': '이름을 입력해주세요'}),
            "password": forms.PasswordInput,
            "password1": forms.PasswordInput,
            "major": forms.TextInput(attrs={'placeholder': '학과을 입력해주세요'}),

        }

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # if not email.endswith('@wku.ac.kr'):
        #     raise ValidationError(
        #         "오직 wku.ac.kr로만 가입가능합니다")

        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 이메일을 가지고 있습니다")
        except models.User.DoesNotExist:
            return email

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다")
        else:
            return password

    def save(self,  *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        
        user.email = email

        user.username = username
        user.set_password(password)

        user.save()


class PasswordResetForm(auth_forms.PasswordResetForm):
    username = auth_forms.UsernameField(label="사용자ID")  # CharField 대신 사용

    # validation 절차:
    # 1. username에 대응하는 User 인스턴스의 존재성 확인
    # 2. username에 대응하는 email과 입력받은 email이 동일한지 확인

    def clean_username(self):
        data = self.cleaned_data['username']
        if not models.User.objects.filter(username=data).exists():
            raise ValidationError("해당 사용자ID가 존재하지 않습니다.")

        return data

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")

        if username and email:
            if models.User.objects.get(username=username).email != email:
                raise ValidationError("사용자의 이메일 주소가 일치하지 않습니다")

    def get_users(self, email=''):
        active_users = models.User.objects.filter(**{
            'username__iexact': self.cleaned_data["username"],

        })
        return (
            u for u in active_users
            if u.has_usable_password()
        )
