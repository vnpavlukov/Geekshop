from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True)  # blank=True field can be empty

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)  # остатки товара на складе
    image = models.ImageField(upload_to='products_images', blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    # CASCADE если удалить категорию, то удалятся и все продукты в ней
    # PROTECT нельзя удалить категорию если есть хоть один продукт

    def __str__(self):
        return f'{self.name} | {self.category.name}'