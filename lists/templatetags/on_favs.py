from django import template
from lists import models as list_models
from django.shortcuts import get_object_or_404

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, products):
    user = context.request.user

    the_list = list_models.List.objects.get(
        user=user, name="My Favourites Houses"
    )
    return products in the_list.products.all()
