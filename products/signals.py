# signals.py
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Product
import cloudinary.uploader


@receiver(pre_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    if instance.image:
        cloudinary.uploader.destroy(instance.image.public_id)

@receiver(pre_save, sender=Product)
def update_product_image(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_image = Product.objects.get(pk=instance.pk).image
        except Product.DoesNotExist:
            return  # Return if the product does not exist yet (new product)
        if old_image and old_image != instance.image:
            cloudinary.uploader.destroy(old_image.public_id)
