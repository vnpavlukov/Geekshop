from django.shortcuts import render


# функции - вьюхи - контроллеры
def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')


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
