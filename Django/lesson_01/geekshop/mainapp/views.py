import datetime
import json
import os
import random

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from .models import ProductCategory, Product


def main(request):
    title = 'shop from Kosarevsky'

    all_products = Product.objects.all()[:180]

    content = {'title': title, 'products': all_products}
    return render(request, 'mainapp/index.html', content)


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    all_products = Product.objects.all().order_by('?')
    all_products = list(all_products)
    return random.choice(all_products)


def get_same_products(hot_product: Product):
    same_products = Product.objects \
                        .filter(category_id=hot_product.id) \
                        .exclude(id=hot_product.id)[:3]
    return same_products


def products(request, pk=None, page=1):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.filter(is_active=True)
    basket = get_basket(request.user)

    if pk:
        if pk == '0':
            category = {'pk': 0, 'name': 'все'}
            a_products = Product.objects.filter(is_active=True,
                                                category__is_active=True)\
                .order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            a_products = Product.objects.\
                filter(category__pk=pk, is_active=True, category__is_active=True)\
                .order_by('price')

        paginator = Paginator(a_products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
            'basket': basket,

        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = Product.objects.all()[3:8]
    # same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    title = 'о нас'
    visit_date = datetime.datetime.now()

    file_name = os.path.join(settings.BASE_DIR, 'locations.json')
    with open(file_name, encoding='utf-8') as f:
        locations = json.load(f)

    content = {'title': title, 'visit_date': visit_date, 'locations': locations}
    return render(request, 'mainapp/contact.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
        'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/product.html', content)
