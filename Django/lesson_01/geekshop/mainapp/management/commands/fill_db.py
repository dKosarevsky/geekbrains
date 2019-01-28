import os
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser

BASE_JSON_PATH = os.path.join(settings.BASE_DIR, 'mainapp', 'json')

def loadFromJSON(file_name):
    with open(os.path.join(BASE_JSON_PATH, f'{file_name}.json')) as f:
        return json.load(f)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = loadFromJSON('categories')
        products = loadFromJSON('products')

        ProductCategory.objects.all().delete()
        Product.objects.all().delete()

        for category in categories:
            ProductCategory.objects.create(**category)
            # new_category.save()

        for product in products:
            category_name = product.pop('category')
            # получаем категорию по имени
            product_category = ProductCategory.objects.get(name=category_name)
            # заменяем название категории объектом
            product['category_id'] = product_category.id
            Product.objects.create(**product)
            # new_product.save()

        # создаем суперпользователя при помощи менеджера модели
        ShopUser.objects.all().delete()
        ShopUser.objects.create_superuser(
            username='django', email='django@geekshop.local', password='geekbrains', age=18
        )
