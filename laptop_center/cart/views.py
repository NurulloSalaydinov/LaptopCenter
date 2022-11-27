import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic import CreateView, View
from django.views.decorators.csrf import csrf_exempt
from common.models import Product
from .models import Cart, CartProduct, Order


def get_user_cart(request):
    try:
        cart = Cart.objects.prefetch_related('products').get(
            id=request.session['user_cart_id'])
    except:
        cart = Cart.objects.prefetch_related(
            'products').create(total_quantity=0, total_cost=0)
        request.session['user_cart_id'] = cart.id
    return cart


def cart_view(request):
    return render(request, 'shopping.html')

def confirm_order(request):
    return render(request, 'confirm.html')

def deleteCartItem(request, product_id, qty):
    cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    cart.deleteItem(product_id, qty)
    messages.add_message(request, messages.INFO, 'Savatchadan o\'chirildi')
    return redirect('cart:my-cart')


@csrf_exempt
def add_to_cart(request):
    d = request.body
    data = json.loads(d)
    product_id = int(data['product_id'])
    quantity = int(data['qty'])
    if not quantity:
        quantity = 0
    cart = get_user_cart(request)
    # first check if product contains in cart then add quantity
    for i in cart.products.all():
        if i.product.id == product_id:
            i.quantity += quantity
            cost = ((i.product.get_cost()) * quantity)
            i.cost += int(i.product.get_cost() * quantity)
            cart.total_quantity += quantity
            cart.total_cost += cost
            i.save()
            cart.save()
            return JsonResponse({'status': 200})
    # if product doesn't exist in cart then add it
    cart.add(product_id, quantity)
    return JsonResponse({'status': 200})


class CheckoutProductView(View):
    def get(self, request, product_id, quantity):
        product = Product.objects.get(id=product_id)
        return render(request, 'order-single.html', {'product': product, 'quantity': quantity, 'cost': product.get_cost() * int(quantity)})

    def post(self, request, product_id, quantity):
        cart = Cart.objects.create()
        cart.add(product_id, quantity)
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        Order.objects.create(cart=cart, **data)
        return redirect('cart:confirm-order')


class CheckoutView(View):
    def get(self, request):
        cart = get_user_cart(request)
        return render(request, 'order.html', {'cart': cart})

    def post(self, request):
        data = request.POST.dict()
        cart = get_user_cart(request)
        del data['csrfmiddlewaretoken']
        request.session['user_cart_id'] = None
        Order.objects.create(cart=cart, **data)
        return redirect('cart:confirm-order')

