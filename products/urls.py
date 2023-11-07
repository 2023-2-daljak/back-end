from django.urls import path
from . import views
from products import views as products_view

app_name = "product"

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("products", products_view.all_products, name="product_list"),
]
