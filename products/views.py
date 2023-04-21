from django.shortcuts import render, HttpResponseRedirect
from products.models import Product, ProductCategory, Basket
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView

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

class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Store"
        return context
# def index(request):
#     return render(request, 'products/index.html')

class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'
    paginate_by = 3
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categorys'] = ProductCategory.objects.all()
        context['title'] = "Store-Каталог"
        return context

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset


# def products(request, category_id=None, page_number=1):
#     products = Product.objects.filter(category__id=category_id) if category_id else Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)
#     context = {
#         'title': 'Store - Каталог',
#         #'products': dic_product,
#         'products': products_paginator,
#         'categorys': ProductCategory.objects.all(),
#     }
#     return render(request, 'products/products.html', context=context)

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