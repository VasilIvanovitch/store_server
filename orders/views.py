from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView


class OrderCreateView(TemplateView):
    # CreateView
    template_name = 'orders/order-create.html'