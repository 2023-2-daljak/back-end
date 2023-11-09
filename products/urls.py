from django.urls import path
from . import views
from products import views as products_view
from django.conf import settings
from django.conf.urls.static import static

app_name = "product"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("products", products_view.all_products, name="product_list"),
    path("search/", products_view.search, name="search"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
