from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import ContactForm
from .models import ( Banner, Product, Category, Brand, Color )


def home_view(request):
    banner = Banner.objects.order_by('-id').select_related('category')
    most_purchased_products = Product.objects.prefetch_related('product_images').filter(most_purchased=True, is_purchased=False).select_related('category', 'brand', 'color')[:4]
    discounted_products = Product.objects.prefetch_related('product_images').filter(
        is_discount=True, is_purchased=False).select_related('category', 'brand', 'color')[:4]
    context = {
        'banners': banner,
        'most_purchased_products': most_purchased_products,
        'discounted_products': discounted_products
    }
    return render(request, 'index.html', context)


def category_related_products(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    categories = Category.objects.all()
    product_list = Product.objects.prefetch_related('product_images').filter(
        category=category, is_purchased=False).select_related('category', 'brand', 'color')
    brands = Brand.objects.all()
    colors = Color.objects.all()
    if request.method == 'GET':
        get_brands = request.GET.getlist('brands')
        get_colors = request.GET.getlist('colors')
        min_price = request.GET.get('minPrice', 1)
        max_price = request.GET.get('maxPrice', 100000)
        price = [min_price, max_price]
        if get_brands:
            product_list = product_list.filter(brand__slug__in=get_brands)
        if get_colors:
            product_list = product_list.filter(color__id__in=get_colors)
        if price:
            product_list = product_list.filter(cost__range=price)


    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'category': category,
        'categories': categories,
        'brands': brands,
        'colors': colors
    }
    return render(request, 'products.html', context)


def shop_products(request):
    categories = Category.objects.all()
    product_list = Product.objects.prefetch_related('product_images').select_related('category', 'brand', 'color').order_by('-id').filter(is_purchased=False)
    brands = Brand.objects.all()
    colors = Color.objects.all()
    if request.method == 'GET':
        get_brands = request.GET.getlist('brands')
        get_colors = request.GET.getlist('colors')
        min_price = request.GET.get('minPrice', 1)
        max_price = request.GET.get('maxPrice', 100000)
        price = [min_price, max_price]
        if get_brands:
            product_list = product_list.filter(brand__slug__in=get_brands)
        if get_colors:
            product_list = product_list.filter(color__id__in=get_colors)
        if price:
            product_list = product_list.filter(cost__range=price)

    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'colors': colors
    }
    return render(request, 'products.html', context)

def shop_products_most_purchased(request):
    categories = Category.objects.all()
    product_list = Product.objects.prefetch_related('product_images').filter(most_purchased=True, is_purchased=False).select_related('category', 'brand', 'color').order_by('-id')
    brands = Brand.objects.all()
    colors = Color.objects.all()
    if request.method == 'GET':
        get_brands = request.GET.getlist('brands')
        get_colors = request.GET.getlist('colors')
        min_price = request.GET.get('minPrice', 1)
        max_price = request.GET.get('maxPrice', 100000)
        price = [min_price, max_price]
        if get_brands:
            product_list = product_list.filter(brand__slug__in=get_brands)
        if get_colors:
            product_list = product_list.filter(color__id__in=get_colors)
        if price:
            product_list = product_list.filter(cost__range=price)

    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'colors': colors
    }
    return render(request, 'products.html', context)

def shop_products_disconts(request):
    categories = Category.objects.all()
    product_list = Product.objects.prefetch_related('product_images').filter(is_discount=True, is_purchased=False).select_related('category', 'brand', 'color').order_by('-id')
    brands = Brand.objects.all()
    colors = Color.objects.all()
    if request.method == 'GET':
        get_brands = request.GET.getlist('brands')
        get_colors = request.GET.getlist('colors')
        min_price = request.GET.get('minPrice', 1)
        max_price = request.GET.get('maxPrice', 100000)
        price = [min_price, max_price]
        if get_brands:
            product_list = product_list.filter(brand__slug__in=get_brands, is_discount=True)
        if get_colors:
            product_list = product_list.filter(color__id__in=get_colors, is_discount=True)
        if price:
            product_list = product_list.filter(cost__range=price, is_discount=True)

    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'colors': colors
    }
    return render(request, 'products.html', context)


def product_detail(request, product_slug):
    product = Product.objects.select_related('category', 'color', 'brand').prefetch_related(
        'product_images').get(slug=product_slug, is_purchased=False)
    related_products = Product.objects.select_related('category', 'color', 'brand').prefetch_related(
        'product_images').filter(category=product.category, is_purchased=False).exclude(id=product.id)[:4]
    context = {
        'object': product,
        'products': related_products
    }
    return render(request, 'about.html', context)


def create_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Sizning so\'rovingiz muvaffaqiyatli yuborildi !')
            return redirect('/')
    else:
        return redirect('/')


def search(request):
    categories = Category.objects.all()
    product_list = Product.objects.prefetch_related('product_images').select_related(
        'category', 'brand', 'color').order_by('-id').filter(is_purchased=False)
    brands = Brand.objects.all()
    colors = Color.objects.all()
    if request.method == 'GET':
        get_brands = request.GET.getlist('brands')
        get_colors = request.GET.getlist('colors')
        min_price = request.GET.get('minPrice', 1)
        max_price = request.GET.get('maxPrice', 100000)
        q = request.GET.get('q', '')
        price = [min_price, max_price]
        if get_brands:
            product_list = product_list.filter(brand__slug__in=get_brands)
        if get_colors:
            product_list = product_list.filter(color__id__in=get_colors)
        if price:
            product_list = product_list.filter(cost__range=price)
        if q:
            product_list = product_list.filter(Q(title__icontains=q) | Q(description__icontains=q))


    paginator = Paginator(product_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj,
        'categories': categories,
        'brands': brands,
        'colors': colors
    }
    return render(request, 'products.html', context)

