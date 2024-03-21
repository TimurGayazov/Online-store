from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_role = models.CharField('Роль пользователя', max_length=200, default='User')


class Category(models.Model):
    category_name = models.CharField('Название категории', max_length=50)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    product_name = models.CharField('Полное название товара', max_length=200)
    product_image = models.ImageField(upload_to='product_img/', null=True, blank=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    description = models.TextField('Описание товара', max_length=500)
    link = models.CharField('Ссылка на товар', max_length=200)
    price = models.FloatField('Цена', max_length=6)

    def __str__(self):
        return f'| {self.product_name} |'

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class Basket(models.Model):
    basket_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    products_id = models.ManyToManyField(Product)

    def get_total_price(self):
        return sum(product.price for product in self.products_id.all())

    def __str__(self):
        return f'| {self.basket_id} basket |'

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'


class Receipt(models.Model):
    user_username = models.CharField('Ник пользователя', max_length=200)
    date = models.CharField('date', max_length=200)
    basket_products = models.ManyToManyField(Product)
    total_price = models.FloatField('Цена', max_length=6)

    def __str__(self):
        return f'| {self.user_username} |'

    class Meta:
        verbose_name = 'Receipt'
        verbose_name_plural = 'Receipts'


class Role(models.Model):
    role_name = models.CharField('Название роли', max_length=50)

    def __str__(self):
        return self.role_name

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'
