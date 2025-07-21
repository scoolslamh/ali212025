from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created_at', 'product_image']
    search_fields = ['name']
    list_filter = ['created_at']
    
    def product_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" style="border-radius: 6px;" />', obj.image.url)
        return "لا توجد صورة"

    product_image.short_description = 'صورة المنتج'
