from rest_framework import serializers
from photos.models import Photo  # photos 앱의 Photo 모델 import
# product_categories 앱의 ProductCategory 모델 import
from product_categories.models import ProductCategory
from users.models import User
from .models import Basket


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = "__all__"
