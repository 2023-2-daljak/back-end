from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

app_name = "user"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("email_verify/", views.email_verify, name="verify"),
    path("verify/<str:key>", views.complete_verification,
         name="complete-verification"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
