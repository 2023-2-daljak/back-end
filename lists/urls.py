from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("toggle/<int:product_pk>", views.toggle_room, name="toggle_room"),
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),]
