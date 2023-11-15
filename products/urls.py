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
    path("products/<int:pk>", views.ProductDetail.as_view(), name="detail"),
    path("products/create", views.CreateProductView.as_view(), name="create"),
    path("<int:pk>/edit", views.EditProjectView.as_view(), name="edit"),
    path('<int:pk>/delete', views.DeleteProductView.as_view(), name='delete'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
