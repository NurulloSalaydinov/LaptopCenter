from django.urls import reverse
from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    title = models.CharField(verbose_name='Kategoriya nomi', max_length=255)
    slug = models.SlugField(verbose_name='Slugi *')

    def get_absolute_url(self):
        return reverse('common:shop-category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Brand(models.Model):
    title = models.CharField(verbose_name='Brand nomi', max_length=255)
    slug = models.SlugField(verbose_name='Slugi *')

    def get_absolute_url(self):
        return reverse('common:brand_related_products', kwargs={'brand_slug': self.slug})

    def __str__(self):
        return f"{self.title}"


class Color(models.Model):
    title = models.CharField(verbose_name='Rangi', max_length=255)
    english_name = models.CharField(verbose_name='Rangning nomi (inglizcha)', max_length=100)

    def __str__(self):
        return f"{self.title}"


class ProductImages(models.Model):
    title = models.CharField(verbose_name='Rasm nomi (agar rasm topilmasa)', max_length=255)
    image = models.ImageField(
        verbose_name='Rasm', upload_to='products/%y-%m-%d')

    def __str__(self):
        return f"{self.title}"


class Banner(models.Model):
    category = models.ForeignKey(
        Category, verbose_name='Banner kategoriyasi', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='Banner nomi', max_length=255)
    description = models.TextField(verbose_name='Banner haqida')
    image = models.ImageField(verbose_name='Banner rasmi', upload_to='banner/%y-%m-%d')

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    title = models.CharField(verbose_name='Tovar nomi', max_length=255)
    slug = models.SlugField(verbose_name='Tovar slugi *')
    description = models.TextField(verbose_name='Tovar haqida')
    cost = models.PositiveIntegerField(verbose_name='Tovar narxi "$" (100)')
    is_discount = models.BooleanField(default=False, verbose_name='Chegirmasi bormi ?')
    discount_percent = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Agar chegirmasi bor bolsa necha foiz')
    most_purchased = models.BooleanField(default=False, verbose_name='Tovar kop sotiladiganmi ?')
    poster = models.ImageField(upload_to='poster/%y/%m/%d/', verbose_name='Tovar posteri')
    product_images = models.ManyToManyField(
        ProductImages, verbose_name='Tovar rasmlari')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Tovar kategoriyasi')
    brand = models.ForeignKey(
        Brand, verbose_name='Tovar brandi', on_delete=models.PROTECT)
    color = models.ForeignKey(
        Color, verbose_name='Tovar rangi', on_delete=models.PROTECT)
    is_purchased = models.BooleanField(default=False, verbose_name='Sotilib bolindimi ?')

    def get_cost(self):
        if self.is_discount and self.discount_percent:
            return (int(self.cost * ( (100 - self.discount_percent) / 100 )))
        else:
            return self.cost
    
    # def get_first_image(self):
    #     return self.product_images.first().image.url

    def get_absolute_url(self):
        return reverse('common:product_details', kwargs={'product_slug': self.slug})

    def __str__(self):
        return f"{self.title}"


# class DiscountProducts(models.Model):
#     product = models.ManyToManyField(Product, related_name="discounted_products")
#     end_date = models.DateField()
#     percent = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.end_date} da tugedi - {self.percent} foizga chegirma"


class Contact(models.Model):
    name = models.CharField(verbose_name='Ism', max_length=255)
    surname = models.CharField(verbose_name='Familya', max_length=255)
    phone = models.CharField(verbose_name='Telefon raqam', max_length=255)
    email = models.EmailField(verbose_name='Email pochta', null=True, blank=True)
    message = models.TextField(verbose_name='Xabar')
    is_pinned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.surname}"

