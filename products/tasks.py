from celery import shared_task
import stripe

from django.conf import settings
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


@shared_task
def create_stripe_product_price(product_id):
    product = Product.objects.get(id=product_id)
    stripe_product = stripe.Product.create(name=product.name)
    stripe_product_price = stripe.Price.create(
        product=stripe_product['id'], unit_amount=round(product.price * 100), currency='byn')
    product.stripe_product_price_id = stripe_product_price['id']
    # product.save()

# @shared_task
# def create_stripe_product_price(product_id):
#     product = Product.objects.get(id=product_id)
#     stripe_product = stripe.Product.create(name=product.name)
#     stripe_product_price = stripe.Price.create(
#         product=stripe_product['id'], unit_amount=round(product.price * 100), currency='byn')
#     product.stripe_product_price_id = stripe_product_price['id']
#     product.save()