from django.db import models
from django.shortcuts import get_object_or_404
from common.models import Product


class CartProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name='Mahsulot', on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(verbose_name='Mahsulot miqdori')
    cost = models.PositiveIntegerField(verbose_name='Mahsulot narxi')

    def __str__(self):
        return f"{self.product.title} - narx {self.cost}"


class Cart(models.Model):
    products = models.ManyToManyField(
        CartProduct, verbose_name='Mahsulotlar', related_name="cart_products", blank=True)
    total_quantity = models.PositiveIntegerField(verbose_name='Jami soni', default=0)
    total_cost = models.PositiveIntegerField(verbose_name='Jami narxi', default=0)

    def add(self, product_id, qty):
        product = Product.objects.get(id=product_id)
        cost = ((product.get_cost()) * qty)
        self.products.create(
            product=product,
            quantity=qty,
            cost=cost
        )
        self.total_quantity += qty
        self.total_cost += cost
        self.save()
        return True

    def deleteItem(self, product_id, qty):
        product = Product.objects.get(id=product_id)
        p_id = product.id
        for item in self.products.all():
            if item.product.id == p_id:
                item.delete()

        cost = ((product.get_cost()) * qty)
        self.total_quantity -= qty
        self.total_cost -= cost
        self.save()
        return True

    def __str__(self):
        return f"CART {self.id} jami soni: {self.total_quantity} jami narxi: {self.total_cost}"


class Order(models.Model):
    PROVINCE = (
        ('Toshkent', 'Toshkent'),
        ('Andijon', 'Andijon'),
        ('Namangan', 'Namangan'),
        ('Farg\'ona', 'Farg\'ona'),
        ('Samarqand', 'Samarqand'),
        ('Jizzax', 'Jizzax'),
        ('Buxoro', 'Buxoro'),
        ('Qashqadaryo', 'Qashqadaryo'),
        ('Surxondaryo', 'Surxondaryo'),
        ('Xorazm', 'Xorazm'),
        ('Navoiy', 'Navoiy'),
        ('Sirdaryo', 'Sirdaryo'),
        ('Qoraqalpogiston', 'Qoraqalpogiston'),
    )
    STATUS = (
        ('Yetkazib berildi', 'Yetkazib berildi'),
        ('Korib chiqilyapti', 'Korib chiqilyapti'),
        ('Korilmadi', 'Korilmadi'),
    )
    cart = models.ForeignKey(Cart, verbose_name='Savatcha', on_delete=models.PROTECT)
    full_name = models.CharField(verbose_name='Toliq ism', max_length=255)
    province = models.CharField(verbose_name='Viloyat', max_length=255, choices=PROVINCE)
    city = models.CharField(verbose_name='Shahar', max_length=255)
    address = models.CharField(verbose_name='Manzil', max_length=255)
    zipcode = models.CharField(verbose_name='Zip ko\'d', max_length=20, blank=True, null=True)
    phone = models.CharField(verbose_name='Telefon raqam', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(verbose_name='Holat', max_length=255, choices=STATUS, default='Korilmadi')

    def __str__(self):
        return f"{self.full_name}"


