from django.views import View
from django.shortcuts import render
from django.views.generic import FormView, DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from . import forms
from . import models
from django.contrib.auth.views import PasswordChangeView
from django.core.paginator import Paginator
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import auth
from django.contrib.auth.models import User  # User model 연결
from django.views.generic import TemplateView
# 오브젝트를 생성하는 뷰 (form 혹은 model과 연결되서 새로운 데이터를 넣을 때 CreateView - generic view를 사용)
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm  >>  장고의 기본 회원가입 폼 (ID, PW만 확인한다 - 뒤에서 이메일 추가 커스터미아징 예정)
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView

# Create your views here.


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                print("hello")
                login(request, user)
                return redirect(reverse("product:home"))
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("product:home"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("user:verify")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


class UserProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"


def email_verify(request):

    return render(request, "users/email_verify.html")


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_confirmed = True
        user.email_secret = ""
        user.save()
        if user is not None:
            auth.login(request, user)
        # to do: add succes message
    except models.User.DoesNotExist:
        # to do: add error message
        pass
    return redirect(reverse("product:home"))


class UpdatePasswordView(PasswordChangeView):

    template_name = "users/update-password.html"


class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy("user:password-verify")
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset.html'
    mail_title = "비밀번호 재설정"

    def form_valid(self, form):
        return super().form_valid(form)


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy("core:project")
    template_name = 'users/password_reset_confirm.html'

    def form_valid(self, form):
        return super().form_valid(form)


def password_verify(request):

    return render(request, "users/password_reset_complete.html")
