from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.contrib.admin.views.decorators import staff_member_required
from cart.models import CartProduct, Cart, Order
from common.models import Category, Product, Brand, Contact, ProductImages, Color, Banner
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator


# category

@method_decorator(staff_member_required, name='dispatch')
class CategoryListView(ListView):
    model = Category
    ordering = ['-id']
    paginate_by = 26
    context_object_name = 'categories'
    template_name = 'master/categories.html'

    def get_queryset(self):
        queryset = super(CategoryListView, self).get_queryset()
        q = self.request.GET.get('q', None)
        if q:
            queryset = Category.objects.filter(title__icontains=q)
        return queryset



@method_decorator(staff_member_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'master/create-update.html'
    success_url = '/master/categories/'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['o'] = 'Kategoriya qo\'shish'
        context['u'] = '/master/categories/'
        return context



@method_decorator(staff_member_required, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/categories/'

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Kategoriyani tahrirlash'
        context['u'] = '/master/categories/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = '/master/categories/'
    template_name = 'master/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['o'] = 'Kategoriyani o\'chirish'
        context['u'] = '/master/categories/'
        return context

# end category
# brand

@method_decorator(staff_member_required, name='dispatch')
class BrandListView(ListView):
    model = Brand
    ordering = ['-id']
    paginate_by = 26
    context_object_name = 'brands'
    template_name = 'master/brands.html'

    def get_queryset(self):
        queryset = super(BrandListView, self).get_queryset()
        q = self.request.GET.get('q', None)
        if q:
            queryset = Brand.objects.filter(title__icontains=q)
        return queryset



@method_decorator(staff_member_required, name='dispatch')
class BrandCreateView(CreateView):
    model = Brand
    template_name = 'master/create-update.html'
    success_url = '/master/brands/'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BrandCreateView, self).get_context_data(**kwargs)
        context['o'] = 'Brend qo\'shish'
        context['u'] = '/master/brands/'
        return context



@method_decorator(staff_member_required, name='dispatch')
class BrandUpdateView(UpdateView):
    model = Brand
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/brands/'

    def get_context_data(self, **kwargs):
        context = super(BrandUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Brendni tahrirlash'
        context['u'] = '/master/brands/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class BrandDeleteView(DeleteView):
    model = Brand
    success_url = '/master/brands/'
    template_name = 'master/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(BrandDeleteView, self).get_context_data(**kwargs)
        context['o'] = 'Brendni o\'chirish'
        context['u'] = '/master/brands/'
        return context

# end brand
# color

@method_decorator(staff_member_required, name='dispatch')
class ColorListView(ListView):
    model = Color
    ordering = ['-id']
    paginate_by = 26
    context_object_name = 'colors'
    template_name = 'master/colors.html'
    
    def get_queryset(self):
        queryset = super(ColorListView, self).get_queryset()
        q = self.request.GET.get('q', None)
        if q:
            queryset = Color.objects.filter(title__icontains=q)
        return queryset



@method_decorator(staff_member_required, name='dispatch')
class ColorCreateView(CreateView):
    model = Color
    template_name = 'master/create-update.html'
    success_url = '/master/colors/'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ColorCreateView, self).get_context_data(**kwargs)
        context['o'] = 'Rang qo\'shish'
        context['u'] = '/master/colors/'
        return context



@method_decorator(staff_member_required, name='dispatch')
class ColorUpdateView(UpdateView):
    model = Color
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/colors/'

    def get_context_data(self, **kwargs):
        context = super(ColorUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Rangni tahrirlash'
        context['u'] = '/master/colors/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class ColorDeleteView(DeleteView):
    model = Color
    success_url = '/master/colors/'
    template_name = 'master/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ColorDeleteView, self).get_context_data(**kwargs)
        context['o'] = 'Rangni o\'chirish'
        context['u'] = '/master/colors/'
        return context

# end color
# banner

@method_decorator(staff_member_required, name='dispatch')
class BannerListView(ListView):
    queryset = Banner.objects.select_related('category')
    paginate_by = 26
    context_object_name = 'banners'
    template_name = 'master/banner.html'

    def get_queryset(self):
        queryset = super(BannerListView, self).get_queryset()
        q = self.request.GET.get('q', '')
        if q:
            queryset = Banner.objects.filter(title__icontains=q).select_related('category')
        return queryset



@method_decorator(staff_member_required, name='dispatch')
class BannerCreateView(CreateView):
    model = Banner
    template_name = 'master/create-update.html'
    success_url = '/master/banner/'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(BannerCreateView, self).get_context_data(**kwargs)
        context['o'] = 'Banner qo\'shish'
        context['u'] = '/master/banner/'
        return context



@method_decorator(staff_member_required, name='dispatch')
class BannerUpdateView(UpdateView):
    model = Banner
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/banner/'

    def get_context_data(self, **kwargs):
        context = super(BannerUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Bannerni tahrirlash'
        context['u'] = '/master/banner/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class BannerDeleteView(DeleteView):
    model = Banner
    success_url = '/master/banner/'
    template_name = 'master/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(BannerDeleteView, self).get_context_data(**kwargs)
        context['o'] = 'Bannerni o\'chirish'
        context['u'] = '/master/banner/'
        return context

# end banner
# product

@method_decorator(staff_member_required, name='dispatch')
class ProductListView(ListView):
    # model = Product
    queryset = Product.objects.prefetch_related(
        'product_images').select_related('category', 'brand', 'color')
    ordering = ['-id']
    paginate_by = 26
    
    context_object_name = 'products'
    template_name = 'master/products.html'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        status = self.request.GET.get('is_purchased', None)
        q = self.request.GET.get('q', '')
        if status:
            queryset = Product.objects.filter(is_purchased=status, title__icontains=q).prefetch_related(
                    'product_images').select_related('category', 'brand', 'color')
        else:
            queryset = Product.objects.filter(title__icontains=q).prefetch_related(
                    'product_images').select_related('category', 'brand', 'color')
        return queryset


@method_decorator(staff_member_required, name='dispatch')
class ProductCreateView(CreateView):
    queryset = Product.objects.prefetch_related(
        'product_images').select_related('category', 'brand', 'color')
    template_name = 'master/create-update.html'
    success_url = '/master/products/'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['o'] = 'Tovar qo\'shish'
        context['u'] = '/master/products/'
        context['product_images'] = ProductImages.objects.all()
        return context


@method_decorator(staff_member_required, name='dispatch')
class ProductUpdateView(UpdateView):
    queryset = Product.objects.prefetch_related(
        'product_images').select_related('category', 'brand', 'color')
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/products/'

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Tovarni tahrirlash'
        context['u'] = '/master/products/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/master/products/'
    template_name = 'master/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['o'] = 'Tovarni o\'chirish'
        context['u'] = '/master/products/'
        return context

# end product

# productimage

@method_decorator(staff_member_required, name='dispatch')
class ProductImageListView(ListView):
    model = ProductImages
    ordering = ['-id']
    paginate_by = 26
    context_object_name = 'product_images'
    template_name = 'master/product_images.html'
    
    def get_queryset(self):
        queryset = super(ProductImageListView, self).get_queryset()
        q = self.request.GET.get('q', None)
        if q:
            queryset = ProductImages.objects.filter(title__icontains=q)
        return queryset


@method_decorator(staff_member_required, name='dispatch')
class ProductImageCreateView(CreateView):
    model = ProductImages
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/product_images/'

    def get_context_data(self, **kwargs):
        context = super(ProductImageCreateView,
                        self).get_context_data(**kwargs)
        context['o'] = 'Tovar rasmini qo\'shish'
        context['u'] = '/master/product_images/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class ProductImageUpdateView(UpdateView):
    model = ProductImages
    fields = '__all__'
    template_name = 'master/create-update.html'
    success_url = '/master/product_images/'

    def get_context_data(self, **kwargs):
        context = super(ProductImageUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Tovar rasmni tahrirlash'
        context['u'] = '/master/product_images/'
        return context


@method_decorator(staff_member_required, name='dispatch')
class ProductImageDeleteView(DeleteView):
    model = ProductImages
    success_url = '/master/product_images/'
    template_name = 'master/confirm.html'

    def get_context_data(self, **kwargs):
        context = super(ProductImageDeleteView,
                        self).get_context_data(**kwargs)
        context['o'] = 'Tovar rasmni o\'chirish'
        context['u'] = '/master/product_images/'
        return context


# endproductimage

# order

@method_decorator(staff_member_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    fields = ['status']
    template_name = 'master/create-update.html'
    success_url = '/master/'

    def get_context_data(self, **kwargs):
        context = super(OrderUpdateView, self).get_context_data(**kwargs)
        context['o'] = 'Buyurtmaning holatini tahrirlash'
        context['u'] = '/master/'
        return context

# endorder

# order cart

def order_cart_detail(request, pk):
    cart = Cart.objects.prefetch_related('products').get(id=pk)
    context = {
        'cart': cart
    }
    return render(request, 'master/order-cart.html', context)

# end order cart

@staff_member_required(login_url='/admin/login/')
def dashboard(request):
    overall_product = Product.objects.all().count
    overall_category = Category.objects.all().count
    overall_brand = Brand.objects.all().count

    if request.method == 'GET':
        status = request.GET.get('status', None)
        q = request.GET.get('q', '')
        if status:
            orders = Order.objects.select_related('cart').filter(
                status__exact=status, full_name__icontains=q)
        else:
            orders = Order.objects.select_related('cart').filter(full_name__icontains=q)


    context = {
        'count_product': overall_product,
        'count_category': overall_category,
        'count_brand': overall_brand,
        'orders': orders,
    }
    return render(request, 'master/dashboard.html', context)


@staff_member_required(login_url='/admin/login/')
def messages(request):
    q = request.GET.get('q', None)
    if q:
        contacts = Contact.objects.filter(Q(name__icontains=q) or Q(
            surname__icontains=q) or Q(message__icontains=q))
    else:
        contacts = Contact.objects.all()
    return render(request, 'master/messages.html', {'messages': contacts})

