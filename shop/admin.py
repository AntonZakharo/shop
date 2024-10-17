from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'stock', 'item_type', 'author', 'genre', 'publish_date')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('item_type', 'author', 'genre', 'publish_date', 'price')


