from django.urls import path
from django.views.decorators.cache import cache_page

from products import views

app_name = 'products'
urlpatterns = [
    #  path('', views.index, name='index'),
    path('', views.ProductsListView.as_view(), name='index'),
    # path('', views.products, name='index'),
    # path('category/<int:category_id>/', cache_page(30)(views.ProductsListView.as_view()), name='category'),
    path('category/<int:category_id>/', views.ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', views.ProductsListView.as_view(), name='paginator'),
    # path('page/<int:page_number>/', views.products, name='paginator'),
    path('baskets/add/<int:product_id>/', views.basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', views.basket_remove, name='basket_remove'),
]
