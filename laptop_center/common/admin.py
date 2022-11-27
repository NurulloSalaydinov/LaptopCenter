from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Brand, Color, Product, ProductImages, Banner, Contact



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id')
    search_fields = ('title',)
    list_display_links = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 26


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title', 'description')
    list_display_links = ('title', 'id')
    list_per_page = 26


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'id')
    search_fields = ('title',)
    list_display_links = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 26


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'english_name', 'id')
    search_fields = ('title',)
    list_editable = ('english_name',)
    list_display_links = ('title', 'id')
    list_per_page = 26


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'id')
    search_fields = ('title',)
    list_display_links = ('title', 'id')
    list_per_page = 26

    def get_image(self, obj):
        return format_html('<img src="{}" width="130px" height="auto">'.format(obj.image.url))


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'is_discount', 'discount_percent', 'most_purchased', 'id')
    list_display_links = ('title',)
    search_fields = ('title', 'description')
    list_filter = ('title', 'cost', 'is_discount', 'most_purchased')
    list_editable = ('cost', 'is_discount', 'discount_percent', 'most_purchased')
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 26


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone', 'is_pinned', 'id')
    list_display_links = ('name', 'surname')
    list_filter = ('is_pinned',)
    list_editable = ('is_pinned',)
    list_per_page = 26
