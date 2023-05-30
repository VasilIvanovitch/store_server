from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import Product
from .tasks import create_stripe_product_price_2


# Signal to trigger the task when a new Product is created

# @receiver(post_save, sender=None)
@receiver(post_save, sender=Product)
def create_stripe_product_price_on_create(sender, instance, created, update_fields, **kwargs):
    if created:
        if not instance.stripe_product_price_id:
            create_stripe_product_price_2.delay(instance.id)
    if not created and (not instance.stripe_product_price_id or instance._price != instance.price):
        create_stripe_product_price_2.delay(instance.id)
