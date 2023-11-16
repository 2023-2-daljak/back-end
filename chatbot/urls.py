from django.urls import path
from . import views

app_name = "chatbot"
urlpatterns = [
    # path('addresses/', views.address_list),
    # path('addresses/<int:pk>/', views.address),
    # path('login/', views.login),
    # path('app_login/', views.app_login),
    # path('admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.chat_service),
]
