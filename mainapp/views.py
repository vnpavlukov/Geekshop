from django.shortcuts import render


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
               'products': [
                   {'name': 'Худи черного цвета с монограммами adidas Originals',
                    'price': '6 090,00',
                    'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                    'photo': '"{% static \'vendor/img/products/Adidas-hoodie.png\' %}"'},

                   {'name': 'Синяя куртка The North Face',
                    'price': '23 725,00',
                    'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                    'photo': '"{% static \'vendor/img/products/Blue-jacket-The-North-Face.png\' %}"'},

                   {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': '3 390,00',
                    'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                    'photo': '"{% static \'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png\' %}"'},

                   {'name': 'Черный рюкзак Nike Heritage',
                    'price': '2 340,00',
                    'description': 'Плотная ткань. Легкий материал.',
                    'photo': '"{% static \'vendor/img/products/Black-Nike-Heritage-backpack.png\' %}"'},

                   {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                    'price': '13 590,00',
                    'description': 'Гладкий кожаный верх. Натуральный материал.',
                    'photo': '"{% static \'vendor/img/products/Black-Dr-Martens-shoes.png\' %}"'},

                   {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                    'price': '2 890,00',
                    'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                    'photo': '"{% static \'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png\' %}"'},
               ],
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
        'promotion': False,
        'product_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00'},
            {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00'},
        ]
    }
    return render(request, 'mainapp/test-context.html', context)
