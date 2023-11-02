from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .serializers import ProductSerializer
from django.views.generic import ListView
from . import models
from datetime import datetime


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Product
    paginate_by = 10
    paginate_orphans = 5
