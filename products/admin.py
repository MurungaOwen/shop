from django.contrib import admin
from django.utils.html import format_html
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    image_preview.short_description = 'Image Preview'

admin.site.site_header = "My Shop"
admin.site.site_title = "My Shop"
admin.site.index_title = "Welcome to MyShop"
admin.site.register(Product, ProductAdmin)