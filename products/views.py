from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .serializers import ProductSerializer
from django.views.generic import ListView
from . import models
from datetime import datetime
from django.shortcuts import render, redirect


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Product
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "rooms"


def all_products(request):
    page = request.GET.get("page")
    all_product = models.Product.objects.all()
    paginator = Paginator(all_product, 2)
    products = paginator.get_page(page)
    print(products)
    return render(request, "products/products.html", context={"potato": products})
