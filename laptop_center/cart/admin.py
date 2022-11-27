from django.contrib import admin
from .models import Order, Cart, CartProduct




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'province', 'zipcode', 'phone', 'status', 'id')
    list_editable = ('status',)
    list_filter = ('status', 'province')
    search_fields = ('full_name', 'province', 'zipcode', 'phone')


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'quantity', 'cost', 'id')
    list_filter = ('quantity', 'id', 'cost')
    search_fields = ('get_product_name', 'id')

    def get_product_name(self, obj):
        return obj.product.title

    get_product_name.short_description = 'Mahsulot nomi'


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_quantity', 'total_cost')
    list_display_links = ('id', 'total_quantity', 'total_cost')
    list_filter = ('id', 'total_cost', 'total_quantity')








