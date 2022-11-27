from django.urls import path
from .import views


app_name = 'cart'


urlpatterns = [
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('me/', views.cart_view, name='my-cart'),
    path('delete_item/<int:product_id>/<int:qty>/', views.deleteCartItem, name='delete-item'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('checkout/<int:product_id>/<int:quantity>/', views.CheckoutProductView.as_view(), name='single-checkout'),
    path('confirm-order/', views.confirm_order, name='confirm-order')
]

