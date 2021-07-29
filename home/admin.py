from django.contrib import admin
from .models import Product, Seller

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","pcode","price","seller","created","modified","category")
    list_filter = ("price",)
    search_fields = ("name","pcode")

@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ("name","contact", "adress")

