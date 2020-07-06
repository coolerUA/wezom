from django.contrib import admin
from market.models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'product_thumbnail']
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)
