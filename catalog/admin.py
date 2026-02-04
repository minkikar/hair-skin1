from django.contrib import admin
from .models import Product, Recommendation

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "product_type", "price", "updated_at")
    search_fields = ("name", "product_type")
    list_filter = ("category",)

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "category", "created_at")
    search_fields = ("full_name", "email")
    list_filter = ("category", "created_at")
    filter_horizontal = ("recommended_products",)