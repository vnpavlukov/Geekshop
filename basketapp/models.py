from django.db import models

from authapp.models import User
from mainapp.models import Product


class Bsket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина дял {self.user.name} | Продукт  {self.product.name}'
