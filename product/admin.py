from django.contrib import admin

from product.models import KorCategory, Products, Basket

admin.site.register(KorCategory)
admin.site.register(Products)
admin.site.register(Basket)

# Register your models here.
