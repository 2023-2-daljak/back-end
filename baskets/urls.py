from django.urls import path
from . import views

urlpatterns = [
    path("", views.Baskets.as_view()),
    path("/<int:pk>", views.BasketDetail.as_view()),
]
