from django.shortcuts import render, HttpResponseRedirect

from product.models import KorCategory, Products, Basket


def index(request):
    con = {
        'title': 'ХҚТУ сатылым қоры'
    }
    return render(request, 'product/index.html', con)


def product(request):
    con = {
        'title': 'Қор каталогы',
        'categories': KorCategory.objects.all(),
        'products': Products.objects.all()
    }
    return render(request, 'product/product.html', con)


def baskett(request, product_id):
    curPage = request.META.get('HTTP_REFERER')
    product = Products.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quant=1)
        return HttpResponseRedirect(curPage)
    else:
        basket = baskets.first()
        basket.quant += 1
        basket.save()
        return HttpResponseRedirect(curPage)

        # basket = Basket(user=request.user, product=product, quant=1)
        # basket.save()


def basketDel(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


