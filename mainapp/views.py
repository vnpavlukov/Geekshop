from django.shortcuts import render


# функции - вьюхи - контроллеры
def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {'title': 'GeekShop - каталог'}
    return render(request, 'mainapp/products.html', context)


def test_context(request):
    context = {
        'title': 'geekshop',
        'header': 'Welcome on the site',
        'username': 'Vladimir Pavlukov',
        'products': [
            {'name': 'худи', 'price': '3 050'},
            {'name': 'ботинки', 'price': '4 080'}
        ]
    }
    return render(request, 'mainapp/test-context.html', context)
