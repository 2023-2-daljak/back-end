from django import template
from lists import models as list_models

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, products):
    user = context.request.user
    the_list = list_models.List.objects.filter(
        user=user, name="My Favourites"
    )
    return products in the_list
