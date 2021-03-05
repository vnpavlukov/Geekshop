import os
import json
from django.shortcuts import render
import datetime

from mainapp.models import ProductCategory, Product


# функции - вьюхи - контроллеры
def index(request):
    context = {'title': 'Geekshop',
               'index_header': 'GeekShop Store',
               'index_text': 'Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! '
                             'Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
               'products_button_name': 'Начать покупки',
               }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'Geekshop - Каталог',
               'buy_button_name': 'Отправить в корзину',
               # 'products': json.load(open(products_file_name, encoding='utf8')),
               'products': Product.objects.all(),
               'categories': ProductCategory.objects.all()
               }
    return render(request, 'mainapp/products.html', context)
