from django.contrib import admin
from .models import Dib


@admin.register(Dib)
class DibAdmin(admin.ModelAdmin):
    list_display=(
        "owner",
        "products",
        
    )
    
    list_filter=(
        "products__categories",
        "owner",
        
    )
