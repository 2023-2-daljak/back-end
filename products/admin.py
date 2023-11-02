from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=(
        "registrant",
        "title",
        "content",
        "price",
        "created_at"
    )


    list_filter=(
        "registrant",
        "price",
        "title",
        "categories",
        
    )