from django.contrib import admin
from .models import ProductReview
# Register your models here.

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display=(
        "title",
        "__str__",
    
    )
    
    list_filter=(
        "rating",
        "product__categories",
        
    )