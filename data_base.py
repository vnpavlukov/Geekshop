# python manage.py shell

from mainapp.models import ProductCategory, Product

category = ProductCategory(name='Одежда', description='Новая одежда')
category.save()  # заденесение данных в БД

ProductCategory.objects.create(name='Новинки')  # так же создание нового объекта в БД, можно не сохранять

ProductCategory.objects.get(id=1)  # получение объекта
category.name  # обращение к его аттрибутам
category.description

ProductCategory.objects.filter(id=2)  # получение списка объектов
ProductCategory.objects.first()
ProductCategory.objects.all()
ProductCategory.objects[1]
