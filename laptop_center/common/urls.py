from django.urls import path
from .import views


app_name = 'common'


urlpatterns = [
    path('', views.home_view, name='home'),
    path('new-contact/', views.create_contact, name='new-contact'),
    path('product/detail/<slug:product_slug>/', views.product_detail, name='product_details'),
    path('shop/', views.shop_products, name='shop-products'),
    path('shop/most-purchased/', views.shop_products_most_purchased, name='shop-most-purchased-products'),
    path('shop/discounts/', views.shop_products_disconts,
         name='shop-discount-products'),
    path('shop/category/<slug:category_slug>/', views.category_related_products, name='shop-category'),
    path('shop/search/', views.search, name='search'),
]

