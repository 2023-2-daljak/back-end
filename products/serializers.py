from rest_framework import serializers
from photos.models import Photo  # photos 앱의 Photo 모델 import
# product_categories 앱의 ProductCategory 모델 import
from product_categories.models import ProductCategory
from users.models import User
from .models import Product


from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
