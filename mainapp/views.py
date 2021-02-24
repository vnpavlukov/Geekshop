from django.shortcuts import render


# функции - вьюхи - контроллеры
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


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
        'promotion': False,
        'product_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
        ]
    }
    return render(request, 'mainapp/test-context.html', context)
