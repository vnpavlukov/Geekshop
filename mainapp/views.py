import os
import json
from django.shortcuts import render
import datetime

from mainapp.models import ProductCategory, Product

products_file_name = os.path.join(os.path.dirname(__file__), 'fixtures/data_products.json')


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


def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Добро пожаловать на сайт',
        'username': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами', 'price': '6 600,00'},
            {'name': 'Синяя куртка', 'price': '23 550,00'},
            {'name': 'Коричневый спортивный топ', 'price': '7 500,00'},
        ],
        'datetime': datetime.datetime.now(),
        'promotion': False,
        'product_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
        ]
    }

    return render(request, 'mainapp/test-context.html', context)
