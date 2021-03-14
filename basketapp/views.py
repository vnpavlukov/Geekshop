from django.shortcuts import HttpResponseRedirect
from django.urls import reverse

from mainapp.models import Product
from basketapp.models import Basket


def basket_add(request, product_id=None):
    product = Product.object.get(id=product_id)
    baskets = Basket.object.filter(user=request.user, product=product)

    if not baskets.exists():
        basket = Basket(user=request.user, product=product)
        basket.quantity == 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity == 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
