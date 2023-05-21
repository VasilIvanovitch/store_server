# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Product
# from .tasks import create_stripe_product_price
#
#
# #Signal to trigger the task when a new Product is created
#
# @receiver(post_save, sender=Product)
# def create_stripe_product_price_on_create(sender, instance, created, **kwargs):
#    if created:
#        create_stripe_product_price.delay(instance.id)
#