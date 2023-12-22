from django.db import models
from users.models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique = True)
    description = models.TextField(null = True, blank= True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits= 8, decimal_places= 2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(b.sum() for b in self)
    def total_quantity(self):
        return sum(b.quantity for b in self)

class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    class Meta:
        verbose_name = 'позицию'
        verbose_name_plural = 'Корзина'

    def __str__(self):
        return f'Корзина для {self.user.username}| Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity






