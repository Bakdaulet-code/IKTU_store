from django.db import models
from user.models import User

# Create your models here.
class KorCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    descr = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Product Category'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField(upload_to='products_images', blank=True)
    descr = models.TextField(blank=True)
    short_descr = models.CharField(max_length=64, blank=True)
    pr = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quant = models.PositiveIntegerField(default=0)
    categ = models.ForeignKey(KorCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.categ.name}'


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quant = models.PositiveIntegerField(default=0)
    created_timest = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Себет: {self.user.username} | Товар {self.product.name}'

    def sum(self):
        return self.quant * self.product.pr