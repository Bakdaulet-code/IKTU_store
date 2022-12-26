from django.urls import path

from product.views import product, baskett, basketDel

app_name = 'product'

urlpatterns = [
    path('', product, name='index'),
    path('baskett/<int:product_id>/', baskett, name='baskett'),
    path('bake/<int:id>/', basketDel, name='basketDel'),
]
