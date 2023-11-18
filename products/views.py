from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from django.core.paginator import Paginator
from .serializers import ProductSerializer
from django.views.generic import ListView, DetailView
from . import models
from datetime import datetime
from django.shortcuts import render, redirect
from users import mixins as user_mixins
from . import models, forms
from django.views.generic import ListView, DetailView, View, UpdateView, FormView, DeleteView
from django.shortcuts import render, redirect, reverse


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Product
    paginate_by = 10
    paginate_orphans = 5
    context_object_name = "rooms"


def all_products(request):
    page = request.GET.get("page")
    all_product = models.Product.objects.all()
    paginator = Paginator(all_product, 6)
    products = paginator.get_page(page)

    shapes_s = models.Species.objects.all()
    mind_s = models.Department.objects.all()
    color_s = models.Grade.objects.all()
    other_s = models.Repair.objects.all()

    return render(request, "products/products.html", context={"potato": products,  "mind": mind_s, "color": color_s, "other": other_s, "shape": shapes_s, })


def search(request):
    city = request.GET.get("city")

    shapes_s = models.Department.objects.all()
    mind_s = models.Species.objects.all()
    color_s = models.Grade.objects.all()
    other_s = models.Repair.objects.all()

    department = request.GET.getlist("department")
    species = request.GET.getlist("species")
    grade = request.GET.getlist("grade")
    repair = request.GET.getlist("repair")

    filter_args = {}

    if len(department) > 0:

        for s_amenity in department:
            filter_args["department__pk"] = int(s_amenity)

    if len(species) > 0:
        for s in species:
            filter_args["species__pk"] = int(s)

    if len(grade) > 0:
        for abc in grade:
            filter_args["grade__pk"] = int(abc)

    if len(repair) > 0:
        for oo in repair:
            filter_args["repair__pk"] = int(oo)

    if 'city' in request.GET:
        filter_args["title__contains"] = city
    picture = models.Product.objects.all().filter(**filter_args)

    query = request.GET.get("query")

    return render(request, "partials/search.html", {"abc": picture, "mind": mind_s, "color": color_s, "other": other_s, "shape": shapes_s, "city": city, 'query': query})


class ProductDetail(DetailView):
    model = models.Product
    context_object_name = "product"


class CreateProductView(user_mixins.LoggedInOnlyView, FormView):

    form_class = forms.CreateProductForm
    template_name = "products/product_create.html"

    def form_valid(self, form):
        project = form.save()
        project.registrant = self.request.user
        project.save()
        # project.success(self.request, "Photo Uploaded")
        return redirect(reverse("product:product_list"))


class EditProjectView(UpdateView):

    model = models.Product
    template_name = "products/product_edit.html"
    fields = (
        "title",
        "content",
        "profile",
        "department",
        "species",
        "grade",
        "repair",
    )

    def get_success_url(self):
        return reverse("product:product_list")


class DeleteProductView(DeleteView):

    model = models.Product
    template_name = "products/product_delete.html"

    def get_success_url(self):
        return reverse("product:product_list")
