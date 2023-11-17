from django.contrib import messages
from django.shortcuts import redirect, reverse
from products import models as product_models
from . import forms


def create_review(request, product_pk):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        room = product_models.Product.objects.get(pk=product_pk)
        if not room:
            return redirect(reverse("product:product_list"))
        if form.is_valid():
            review = form.save()
            review.product = room
            review.user = request.user
            review.save()
            messages.success(request, "Product reviewed")
            return redirect(reverse("product:detail", kwargs={"pk": room.pk}))
