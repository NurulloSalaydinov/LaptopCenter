from .views import get_user_cart


def cart_context(request):
    cart = get_user_cart(request)
    context = {
        'cart': cart
    }
    return context
