from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from products import models as room_models
from . import models


def toggle_room(request, product_pk):
    # action = request.GET.get("action", None)
    room = room_models.Product.objects.get(pk=product_pk)
    if room is not None:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="My Favourites Houses"
        )

    the_list.products.add(room)

    return redirect(reverse("product:detail", kwargs={"pk": product_pk}))


class SeeFavsView(TemplateView):

    template_name = "lists/list_detail.html"
