from django.contrib import admin
from .models import Product
from . import models


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "registrant",
        "title",
        "content",
        "created_at"
    )

    list_filter = (
        "registrant",
        "title",
        "categories",

    )


@admin.register(models.Species, models.Grade, models.Repair, models.Department, models.Category, models.TeamNumber)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", )

    def used_by(self, obj):
        return obj.rooms.count()

    pass
