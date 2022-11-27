from django.urls import path
from .import views

app_name = 'master'


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('messages/', views.messages, name='messages'),
    # category
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/create/', views.CategoryCreateView.as_view(),
         name='create-category'),
    path('categories/update/<int:pk>/',
         views.CategoryUpdateView.as_view(), name='update-category'),
    path('categories/delete/<int:pk>/',
         views.CategoryDeleteView.as_view(), name='delete-category'),
    # end category
    # brand
    path('brands/', views.BrandListView.as_view(), name='brands'),
    path('brands/create/', views.BrandCreateView.as_view(),
         name='create-brand'),
    path('brands/update/<int:pk>/',
         views.BrandUpdateView.as_view(), name='update-brand'),
    path('brands/delete/<int:pk>/',
         views.BrandDeleteView.as_view(), name='delete-brand'),
    # end brand
    # color
    path('colors/', views.ColorListView.as_view(), name='colors'),
    path('colors/create/', views.ColorCreateView.as_view(),
         name='create-color'),
    path('colors/update/<int:pk>/',
         views.ColorUpdateView.as_view(), name='update-color'),
    path('colors/delete/<int:pk>/',
         views.ColorDeleteView.as_view(), name='delete-color'),
    # end color
    # banner
    path('banner/', views.BannerListView.as_view(), name='banner'),
    path('banner/create/', views.BannerCreateView.as_view(),
         name='create-banner'),
    path('banner/update/<int:pk>/',
         views.BannerUpdateView.as_view(), name='update-banner'),
    path('banner/delete/<int:pk>/',
         views.BannerDeleteView.as_view(), name='delete-banner'),
    # end banner
    # product
    path('products/', views.ProductListView.as_view(), name='products'),
    path('products/create/', views.ProductCreateView.as_view(),
         name='create-product'),
    path('products/update/<int:pk>/',
         views.ProductUpdateView.as_view(), name='update-product'),
    path('products/delete/<int:pk>/',
         views.ProductDeleteView.as_view(), name='delete-product'),
    # end product
    # product images
   	path('product_images/', views.ProductImageListView.as_view(), name='product-images'),
    path('product_images/update/<int:pk>/',
         views.ProductImageUpdateView.as_view(), name='update-product-image'),
    path('product_images/delete/<int:pk>/',
         views.ProductImageDeleteView.as_view(), name='delete-product-image'),
    path('product_images/create/', views.ProductImageCreateView.as_view(),
         name='create-product-image'),
     # end product images
     # order update
     path('order/update/<int:pk>/', views.OrderUpdateView.as_view(), name='order-update'),
     # endorder update
     path('order/cart/<int:pk>/', views.order_cart_detail, name='order-cart')
]
