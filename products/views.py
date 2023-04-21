from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

dic_product = [
    {
        "image": "/static/vendor/img/products/Adidas-hoodie.png",
        "name": "Худи черного цвета с монограммами adidas Originals",
        "price": 6090,
        "description": "Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.",
    },
    {
        "image": "/static/vendor/img/products/Blue-jacket-The-North-Face.png",
        "name": "Синяя куртка The North Face",
        "price": 23725,
        "description": "Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.",
    },
    {
        "image": "/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png",
        "name": "Коричневый спортивный oversized-топ ASOS DESIGN",
        "price": 3390,
        "description": "Материал с плюшевой текстурой. Удобный и мягкий.",
    },
    {
        "image": "/static/vendor/img/products/Black-Nike-Heritage-backpack.png",
        "name": "Черный рюкзак Nike Heritage",
        "price": 2340,
        "description": "Черный рюкзак Nike Heritage",
    },
    {
        "image": "/static/vendor/img/products/Black-Dr-Martens-shoes.png",
        "name": "Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex",
        "price": 13590,
        "description": "Гладкий кожаный верх. Натуральный материал.",
    },
    {
        "image": "/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png",
        "name": "Темно-синие широкие строгие брюки ASOS DESIGN",
        "price": 2890,
        "description": "Легкая эластичная ткань сирсакер Фактурная ткань.",
    },
]

def index(request):

    return render(request, 'products/index.html')

def products(request, category_id=None, page_number=1):
    products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'title': 'Store - Каталог',
        #'products': dic_product,
        'products': products_paginator,
        'categorys': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context=context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    Basket.objects.get(id=basket_id).delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])