from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from products import models as room_models
from . import models


def toggle_room(request, pk):
    action = request.GET.get("action", None)
    room = room_models.Product.objects.get_or_none(pk=pk)
    if room is not None and action is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favourites Houses"
        )
        if action == "add":
            the_list.products.add(room)
        elif action == "remove":
            the_list.products.remove(room)
    return redirect(reverse("product:product_list", kwargs={"pk": pk}))


class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
