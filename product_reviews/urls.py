from django.urls import path
from . import views


app_name = "reviews"

urlpatterns = [path("create/<int:product_pk>",
                    views.create_review, name="create")]
